import httpx
import pytest
import respx

from nansen import (
    AuthenticationError,
    BadRequestError,
    GatewayTimeoutError,
    InternalServerError,
    Nansen,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)


@pytest.fixture
def client():
    with Nansen(api_key="test-key", max_retries=0) as c:
        yield c


class TestExceptionMapping:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_400_bad_request(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                400,
                json={"error": {"code": "BAD_REQUEST", "message": "Invalid params"}},
            )
        )
        with pytest.raises(BadRequestError) as exc_info:
            client.smart_money.holdings(chains=["ethereum"])
        assert exc_info.value.status_code == 400
        assert "Invalid params" in str(exc_info.value)

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_401_authentication(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                401,
                json={"error": {"code": "UNAUTHORIZED", "message": "Invalid API key"}},
            )
        )
        with pytest.raises(AuthenticationError) as exc_info:
            client.smart_money.holdings(chains=["ethereum"])
        assert exc_info.value.status_code == 401

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_403_permission_denied(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                403,
                json={"error": {"code": "FORBIDDEN", "message": "Insufficient tier"}},
            )
        )
        with pytest.raises(PermissionDeniedError):
            client.smart_money.holdings(chains=["ethereum"])

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_404_not_found(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                404,
                json={"error": {"code": "NOT_FOUND", "message": "Not found"}},
            )
        )
        with pytest.raises(NotFoundError):
            client.smart_money.holdings(chains=["ethereum"])

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_422_unprocessable(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                422,
                json={
                    "detail": [{"loc": ["body", "chains"], "msg": "required", "type": "missing"}]
                },
            )
        )
        with pytest.raises(UnprocessableEntityError):
            client.smart_money.holdings(chains=["ethereum"])

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_429_rate_limit(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                429,
                json={"error": {"code": "RATE_LIMITED", "message": "Too many requests"}},
                headers={"retry-after": "2"},
            )
        )
        with pytest.raises(RateLimitError) as exc_info:
            client.smart_money.holdings(chains=["ethereum"])
        assert exc_info.value.retry_after == 2.0

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_500_internal(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                500,
                json={"error": {"code": "INTERNAL", "message": "Server error"}},
            )
        )
        with pytest.raises(InternalServerError):
            client.smart_money.holdings(chains=["ethereum"])

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_504_gateway_timeout(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                504,
                json={"error": {"code": "TIMEOUT", "message": "Gateway timeout"}},
            )
        )
        with pytest.raises(GatewayTimeoutError):
            client.smart_money.holdings(chains=["ethereum"])

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_error_body_access(self, respx_mock, client):
        body = {"error": {"code": "BAD_REQUEST", "message": "Invalid params"}}
        respx_mock.post("/smart-money/holdings").mock(return_value=httpx.Response(400, json=body))
        with pytest.raises(BadRequestError) as exc_info:
            client.smart_money.holdings(chains=["ethereum"])
        assert exc_info.value.body == body
        assert exc_info.value.response.status_code == 400
