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


class TestAddressCurrentBalance:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_current_balance(self, respx_mock, client):
        respx_mock.post("/profiler/address/current-balance").mock(
            return_value=_paginated_response([
                {
                    "chain": "ethereum",
                    "address": "0xabc",
                    "token_symbol": "ETH",
                    "token_address": "0x0",
                    "value_usd": 10000.0,
                }
            ])
        )
        page = client.profiler.address.current_balance(
            chain="ethereum", address="0xabc"
        )
        assert page.data[0].token_symbol == "ETH"
        assert page.data[0].value_usd == 10000.0

    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_current_balance_with_entity(self, respx_mock, client):
        route = respx_mock.post("/profiler/address/current-balance").mock(
            return_value=_paginated_response([])
        )
        client.profiler.address.current_balance(
            chain="ethereum", entity_name="Vitalik Buterin"
        )
        import json

        body = json.loads(route.calls[0].request.content)
        assert body["entity_name"] == "Vitalik Buterin"
        assert "address" not in body  # NOT_GIVEN stripped


class TestAddressHistoricalBalances:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_historical_balances(self, respx_mock, client):
        respx_mock.post("/profiler/address/historical-balances").mock(
            return_value=_paginated_response([
                {
                    "block_timestamp": "2024-01-01T00:00:00Z",
                    "token_symbol": "ETH",
                    "token_address": "0x0",
                    "chain": "ethereum",
                    "token_amount": 100.0,
                    "value_usd": 300000.0,
                }
            ])
        )
        page = client.profiler.address.historical_balances(
            chain="ethereum",
            date={"from": "2024-01-01", "to": "2024-01-31"},
            address="0xabc",
        )
        assert page.data[0].value_usd == 300000.0


class TestAddressTransactions:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_transactions(self, respx_mock, client):
        respx_mock.post("/profiler/address/transactions").mock(
            return_value=_paginated_response([
                {
                    "chain": "ethereum",
                    "method": "transfer",
                    "volume_usd": 5000.0,
                    "block_timestamp": "2024-01-01T00:00:00Z",
                    "transaction_hash": "0x123",
                    "source_type": "token",
                }
            ])
        )
        page = client.profiler.address.transactions(
            address="0xabc",
            chain="ethereum",
            date={"from": "2024-01-01", "to": "2024-01-31"},
        )
        assert page.data[0].method == "transfer"


class TestAddressCounterparties:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_counterparties(self, respx_mock, client):
        respx_mock.post("/profiler/address/counterparties").mock(
            return_value=_paginated_response([
                {
                    "counterparty_address": "0xdef",
                    "counterparty_address_label": ["Uniswap V3"],
                    "interaction_count": 50,
                    "total_volume_usd": 100000.0,
                    "volume_in_usd": 60000.0,
                    "volume_out_usd": 40000.0,
                }
            ])
        )
        page = client.profiler.address.counterparties(
            chain="ethereum",
            date={"from": "2024-01-01", "to": "2024-01-31"},
            address="0xabc",
        )
        assert page.data[0].interaction_count == 50


class TestAddressRelatedWallets:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_related_wallets(self, respx_mock, client):
        respx_mock.post("/profiler/address/related-wallets").mock(
            return_value=_paginated_response([
                {
                    "address": "0xdef",
                    "relation": "funding",
                    "transaction_hash": "0x123",
                    "block_timestamp": "2024-01-01T00:00:00Z",
                    "order": 1,
                    "chain": "ethereum",
                }
            ])
        )
        page = client.profiler.address.related_wallets(
            address="0xabc", chain="ethereum"
        )
        assert page.data[0].relation == "funding"


class TestPnlSummary:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_pnl_summary(self, respx_mock, client):
        respx_mock.post("/profiler/address/pnl-summary").mock(
            return_value=httpx.Response(
                200,
                json={
                    "realized_pnl_usd": 50000.0,
                    "win_rate": 0.65,
                    "traded_token_count": 20,
                    "traded_times": 100,
                    "realized_pnl_percent": 25.0,
                    "top5_tokens": [],
                },
            )
        )
        resp = client.profiler.pnl_summary(
            chain="ethereum",
            date={"from": "2024-01-01", "to": "2024-01-31"},
            address="0xabc",
        )
        assert resp.data.realized_pnl_usd == 50000.0
        assert resp.data.win_rate == 0.65


class TestPnl:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_pnl(self, respx_mock, client):
        respx_mock.post("/profiler/address/pnl").mock(
            return_value=_paginated_response([
                {
                    "token_symbol": "ETH",
                    "token_address": "0x0",
                    "pnl_usd_realised": 10000.0,
                    "roi_percent_realised": 25.0,
                }
            ])
        )
        page = client.profiler.pnl(chain="ethereum", address="0xabc")
        assert page.data[0].pnl_usd_realised == 10000.0


class TestEntitySearch:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_entity_search(self, respx_mock, client):
        respx_mock.post("/search/entity-name").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": [
                        {"entity_name": "Vitalik Buterin"},
                        {"entity_name": "Vitalik.eth"},
                    ]
                },
            )
        )
        resp = client.profiler.entity_search(search_query="Vitalik")
        assert len(resp.data) == 2
        assert resp.data[0].entity_name == "Vitalik Buterin"


class TestPerpLeaderboard:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_perp_leaderboard(self, respx_mock, client):
        respx_mock.post("/perp-leaderboard").mock(
            return_value=_paginated_response([
                {
                    "trader_address": "0xabc",
                    "total_pnl": 500000.0,
                    "roi": 150.0,
                    "account_value": 1000000.0,
                }
            ])
        )
        page = client.profiler.perp_leaderboard(
            date={"from": "2024-01-01", "to": "2024-01-31"}
        )
        assert page.data[0].total_pnl == 500000.0
