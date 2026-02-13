import httpx
import pytest
import respx

from nansen import BadRequestError, InternalServerError, Nansen
from nansen._utils._retry import calculate_retry_delay


class TestRetryDelay:
    def test_exponential_backoff(self):
        d0 = calculate_retry_delay(0)
        d1 = calculate_retry_delay(1)
        d2 = calculate_retry_delay(2)
        # With jitter, d0 in [0.25, 0.5], d1 in [0.5, 1.0], d2 in [1.0, 2.0]
        assert 0.2 <= d0 <= 0.6
        assert 0.4 <= d1 <= 1.1
        assert 0.8 <= d2 <= 2.2

    def test_max_delay_cap(self):
        delay = calculate_retry_delay(10)  # Would be 512 without cap
        assert delay <= 8.0

    def test_retry_after_header_respected(self):
        delay = calculate_retry_delay(0, retry_after_header="5.0")
        assert delay >= 5.0

    def test_retry_after_header_invalid(self):
        delay = calculate_retry_delay(0, retry_after_header="invalid")
        assert 0.2 <= delay <= 0.6


class TestRetryBehavior:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_retries_on_500(self, respx_mock):
        respx_mock.post("/smart-money/holdings").mock(
            side_effect=[
                httpx.Response(500, json={"error": {"message": "Server error"}}),
                httpx.Response(
                    200,
                    json={
                        "data": [{"token_symbol": "ETH"}],
                        "pagination": {"page": 1, "per_page": 10, "is_last_page": True},
                    },
                ),
            ]
        )
        with Nansen(api_key="test-key", max_retries=1) as client:
            page = client.smart_money.holdings(chains=["ethereum"])
            assert page.data[0].token_symbol == "ETH"

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_retries_on_429(self, respx_mock):
        respx_mock.post("/smart-money/holdings").mock(
            side_effect=[
                httpx.Response(
                    429,
                    json={"error": {"message": "Rate limited"}},
                    headers={"retry-after": "0"},
                ),
                httpx.Response(
                    200,
                    json={
                        "data": [{"token_symbol": "ETH"}],
                        "pagination": {"page": 1, "per_page": 10, "is_last_page": True},
                    },
                ),
            ]
        )
        with Nansen(api_key="test-key", max_retries=1) as client:
            page = client.smart_money.holdings(chains=["ethereum"])
            assert page.data[0].token_symbol == "ETH"

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_no_retry_on_400(self, respx_mock):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(400, json={"error": {"message": "Bad request"}})
        )
        with Nansen(api_key="test-key", max_retries=2) as client:
            with pytest.raises(BadRequestError):
                client.smart_money.holdings(chains=["ethereum"])
        # Only 1 call made (no retries for 400)
        assert respx_mock.calls.call_count == 1

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_exhausted_retries_raises(self, respx_mock):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(500, json={"error": {"message": "Server error"}})
        )
        with Nansen(api_key="test-key", max_retries=1) as client:
            with pytest.raises(InternalServerError):
                client.smart_money.holdings(chains=["ethereum"])
        assert respx_mock.calls.call_count == 2  # initial + 1 retry
