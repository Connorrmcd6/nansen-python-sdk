import httpx
import pytest
import respx

from nansen import Nansen


@pytest.fixture
def client():
    with Nansen(api_key="test-key") as c:
        yield c


class TestDefiHoldings:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_defi_holdings(self, respx_mock, client):
        respx_mock.post("/portfolio/defi-holdings").mock(
            return_value=httpx.Response(
                200,
                json={
                    "summary": {
                        "total_value_usd": 500000.0,
                        "total_assets_usd": 480000.0,
                        "total_debts_usd": 20000.0,
                        "total_rewards_usd": 5000.0,
                        "token_count": 15,
                        "protocol_count": 5,
                    },
                    "protocols": [
                        {
                            "protocol_name": "Aave V3",
                            "chain": "ethereum",
                            "total_value_usd": 200000.0,
                            "total_assets_usd": 190000.0,
                            "total_debts_usd": 10000.0,
                            "total_rewards_usd": 2000.0,
                            "tokens": [
                                {
                                    "symbol": "ETH",
                                    "amount": 50.0,
                                    "value_usd": 150000.0,
                                    "position_type": "deposit",
                                }
                            ],
                        }
                    ],
                },
            )
        )
        resp = client.portfolio.defi_holdings(wallet_address="0xabc")
        assert resp.data.summary.total_value_usd == 500000.0
        assert resp.data.protocols[0].protocol_name == "Aave V3"
        assert resp.data.protocols[0].tokens[0].symbol == "ETH"

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_defi_holdings_request_body(self, respx_mock, client):
        route = respx_mock.post("/portfolio/defi-holdings").mock(
            return_value=httpx.Response(
                200,
                json={"summary": {}, "protocols": []},
            )
        )
        client.portfolio.defi_holdings(wallet_address="0xabc123")
        import json

        body = json.loads(route.calls[0].request.content)
        assert body["wallet_address"] == "0xabc123"
