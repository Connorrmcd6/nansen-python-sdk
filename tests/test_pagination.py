import httpx
import pytest
import respx

from nansen import Nansen


@pytest.fixture
def client():
    with Nansen(api_key="test-key") as c:
        yield c


class TestPagination:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_single_page(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": [
                        {"token_symbol": "ETH", "value_usd": 1000.0},
                        {"token_symbol": "BTC", "value_usd": 2000.0},
                    ],
                    "pagination": {"page": 1, "per_page": 10, "is_last_page": True},
                },
            )
        )
        page = client.smart_money.holdings(chains=["ethereum"])
        assert len(page) == 2
        assert page.data[0].token_symbol == "ETH"
        assert page.data[1].value_usd == 2000.0
        assert not page.has_next_page

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_auto_pagination(self, respx_mock, client):
        # Page 1
        respx_mock.post("/smart-money/holdings").mock(
            side_effect=[
                httpx.Response(
                    200,
                    json={
                        "data": [{"token_symbol": "ETH", "value_usd": 1000.0}],
                        "pagination": {"page": 1, "per_page": 1, "is_last_page": False},
                    },
                ),
                httpx.Response(
                    200,
                    json={
                        "data": [{"token_symbol": "BTC", "value_usd": 2000.0}],
                        "pagination": {"page": 2, "per_page": 1, "is_last_page": True},
                    },
                ),
            ]
        )
        page = client.smart_money.holdings(chains=["ethereum"])
        items = list(page)
        assert len(items) == 2
        assert items[0].token_symbol == "ETH"
        assert items[1].token_symbol == "BTC"

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_iter_pages(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            side_effect=[
                httpx.Response(
                    200,
                    json={
                        "data": [{"token_symbol": "ETH"}],
                        "pagination": {"page": 1, "per_page": 1, "is_last_page": False},
                    },
                ),
                httpx.Response(
                    200,
                    json={
                        "data": [{"token_symbol": "BTC"}],
                        "pagination": {"page": 2, "per_page": 1, "is_last_page": True},
                    },
                ),
            ]
        )
        page = client.smart_money.holdings(chains=["ethereum"])
        pages = list(page.iter_pages())
        assert len(pages) == 2
        assert pages[0].data[0].token_symbol == "ETH"
        assert pages[1].data[0].token_symbol == "BTC"

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_has_next_page(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": [{"token_symbol": "ETH"}],
                    "pagination": {"page": 1, "per_page": 10, "is_last_page": False},
                },
            )
        )
        page = client.smart_money.holdings(chains=["ethereum"])
        assert page.has_next_page

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_extra_fields_allowed(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": [
                        {
                            "token_symbol": "ETH",
                            "value_usd": 1000.0,
                            "new_future_field": "hello",
                        }
                    ],
                    "pagination": {"page": 1, "per_page": 10, "is_last_page": True},
                },
            )
        )
        page = client.smart_money.holdings(chains=["ethereum"])
        item = page.data[0]
        assert item.token_symbol == "ETH"
        # extra="allow" means unknown fields don't raise
        assert item.new_future_field == "hello"  # type: ignore[attr-defined]
