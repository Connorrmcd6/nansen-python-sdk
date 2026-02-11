import httpx
import pytest
import respx

from nansen import Nansen


@pytest.fixture
def client():
    with Nansen(api_key="test-key") as c:
        yield c


def _paginated_response(data):
    return httpx.Response(
        200,
        json={
            "data": data,
            "pagination": {"page": 1, "per_page": 10, "is_last_page": True},
        },
    )


class TestSmartMoneyNetflow:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_netflow(self, respx_mock, client):
        respx_mock.post("/smart-money/netflow").mock(
            return_value=_paginated_response(
                [
                    {
                        "token_symbol": "ETH",
                        "net_flow_24h_usd": 1000000.0,
                        "chain": "ethereum",
                        "token_address": "0x0",
                        "token_sectors": ["DeFi"],
                        "trader_count": 50,
                        "token_age_days": 365,
                    }
                ]
            )
        )
        page = client.smart_money.netflow(chains=["ethereum"])
        assert len(page) == 1
        assert page.data[0].token_symbol == "ETH"
        assert page.data[0].net_flow_24h_usd == 1000000.0


class TestSmartMoneyDexTrades:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_dex_trades(self, respx_mock, client):
        respx_mock.post("/smart-money/dex-trades").mock(
            return_value=_paginated_response(
                [
                    {
                        "chain": "ethereum",
                        "trader_address": "0xabc",
                        "token_bought_symbol": "ETH",
                        "token_sold_symbol": "USDC",
                        "trade_value_usd": 50000.0,
                        "block_timestamp": "2024-01-01T00:00:00Z",
                        "transaction_hash": "0x123",
                        "trader_address_label": "Smart Trader",
                        "token_bought_address": "0x0",
                        "token_sold_address": "0x1",
                        "token_bought_age_days": 100,
                        "token_sold_age_days": 200,
                    }
                ]
            )
        )
        page = client.smart_money.dex_trades(chains=["ethereum"])
        assert page.data[0].trade_value_usd == 50000.0


class TestSmartMoneyPerpTrades:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_perp_trades(self, respx_mock, client):
        respx_mock.post("/smart-money/perp-trades").mock(
            return_value=_paginated_response(
                [
                    {
                        "trader_address": "0xabc",
                        "trader_address_label": "Fund",
                        "token_symbol": "BTC",
                        "side": "Long",
                        "action": "Buy - Open Long",
                        "value_usd": 100000.0,
                        "type": "Market",
                        "block_timestamp": "2024-01-01T00:00:00Z",
                        "transaction_hash": "0x123",
                    }
                ]
            )
        )
        page = client.smart_money.perp_trades()
        assert page.data[0].side == "Long"


class TestSmartMoneyDcas:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_dcas(self, respx_mock, client):
        respx_mock.post("/smart-money/dcas").mock(
            return_value=_paginated_response(
                [
                    {
                        "trader_address": "abc123",
                        "input_token_symbol": "USDC",
                        "output_token_symbol": "SOL",
                        "dca_status": "active",
                        "dca_created_at": "2024-01-01T00:00:00Z",
                        "dca_updated_at": "2024-01-02T00:00:00Z",
                        "transaction_hash": "0x123",
                        "trader_address_label": "Smart Trader",
                        "dca_vault_address": "vault123",
                        "input_token_address": "0x0",
                        "output_token_address": "0x1",
                    }
                ]
            )
        )
        page = client.smart_money.dcas()
        assert page.data[0].dca_status == "active"


class TestSmartMoneyHoldings:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_holdings(self, respx_mock, client):
        respx_mock.post("/smart-money/holdings").mock(
            return_value=_paginated_response(
                [
                    {
                        "chain": "ethereum",
                        "token_symbol": "ETH",
                        "token_address": "0x0",
                        "token_sectors": ["DeFi"],
                        "value_usd": 5000000.0,
                        "holders_count": 100,
                        "token_age_days": 365,
                    }
                ]
            )
        )
        page = client.smart_money.holdings(chains=["ethereum"])
        assert page.data[0].value_usd == 5000000.0
        assert page.data[0].holders_count == 100

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_holdings_with_filters(self, respx_mock, client):
        route = respx_mock.post("/smart-money/holdings").mock(return_value=_paginated_response([]))
        client.smart_money.holdings(
            chains=["ethereum", "base"],
            filters={"value_usd": {"min": 1000}},
            pagination={"page": 1, "per_page": 50},
        )
        request = route.calls[0].request
        import json

        body = json.loads(request.content)
        assert body["chains"] == ["ethereum", "base"]
        assert body["filters"]["value_usd"]["min"] == 1000
        assert body["pagination"]["per_page"] == 50


class TestSmartMoneyHistoricalHoldings:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_historical_holdings(self, respx_mock, client):
        respx_mock.post("/smart-money/historical-holdings").mock(
            return_value=_paginated_response(
                [
                    {
                        "date": "2024-01-01",
                        "chain": "ethereum",
                        "token_symbol": "ETH",
                        "token_address": "0x0",
                        "token_sectors": [],
                        "smart_money_labels": ["Fund"],
                        "holders_count": 50,
                        "token_age_days": 365,
                    }
                ]
            )
        )
        page = client.smart_money.historical_holdings(
            date_range={"from": "2024-01-01", "to": "2024-01-31"},
            chains=["ethereum"],
        )
        assert page.data[0].date == "2024-01-01"
