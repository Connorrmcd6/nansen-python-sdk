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


class TestTokenScreener:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_token_screener(self, respx_mock, client):
        respx_mock.post("/token-screener").mock(
            return_value=_paginated_response([
                {
                    "chain": "ethereum",
                    "token_address": "0x0",
                    "token_symbol": "PEPE",
                    "market_cap_usd": 1000000000.0,
                    "price_usd": 0.00001,
                    "volume": 50000000.0,
                }
            ])
        )
        page = client.tgm.token_screener(chains=["ethereum"])
        assert page.data[0].token_symbol == "PEPE"
        assert page.data[0].market_cap_usd == 1000000000.0


class TestTokenInformation:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_token_information(self, respx_mock, client):
        respx_mock.post("/tgm/token-information").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": {
                        "name": "Pepe",
                        "symbol": "PEPE",
                        "contract_address": "0x0",
                        "logo": "https://example.com/pepe.png",
                        "token_details": {
                            "market_cap_usd": 1000000000.0,
                        },
                        "spot_metrics": {
                            "volume_total_usd": 50000000.0,
                            "total_holders": 100000,
                        },
                    }
                },
            )
        )
        resp = client.tgm.token_information(
            chain="ethereum", token_address="0x0", timeframe="24h"
        )
        assert resp.data.data.name == "Pepe"
        assert resp.data.data.spot_metrics.total_holders == 100000


class TestFlowIntel:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_flow_intel(self, respx_mock, client):
        respx_mock.post("/tgm/flow-intelligence").mock(
            return_value=_paginated_response([
                {
                    "whale_net_flow_usd": 5000000.0,
                    "smart_trader_net_flow_usd": 2000000.0,
                }
            ])
        )
        page = client.tgm.flow_intel(chain="ethereum", token_address="0x0")
        assert page.data[0].whale_net_flow_usd == 5000000.0


class TestHolders:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_holders(self, respx_mock, client):
        respx_mock.post("/tgm/holders").mock(
            return_value=_paginated_response([
                {
                    "address": "0xabc",
                    "address_label": "Whale",
                    "token_amount": 1000000.0,
                    "value_usd": 500000.0,
                    "ownership_percentage": 0.5,
                }
            ])
        )
        page = client.tgm.holders(chain="ethereum", token_address="0x0")
        assert page.data[0].ownership_percentage == 0.5


class TestFlows:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_flows(self, respx_mock, client):
        respx_mock.post("/tgm/flows").mock(
            return_value=_paginated_response([
                {
                    "date": "2024-01-01",
                    "value_usd": 1000000.0,
                    "holders_count": 500,
                }
            ])
        )
        page = client.tgm.flows(
            chain="ethereum",
            token_address="0x0",
            date={"from": "2024-01-01", "to": "2024-01-31"},
        )
        assert page.data[0].holders_count == 500


class TestWhoBoughtSold:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_who_bought_sold(self, respx_mock, client):
        respx_mock.post("/tgm/who-bought-sold").mock(
            return_value=_paginated_response([
                {
                    "address": "0xabc",
                    "bought_volume_usd": 50000.0,
                    "sold_volume_usd": 10000.0,
                }
            ])
        )
        page = client.tgm.who_bought_sold(
            chain="ethereum",
            token_address="0x0",
            date={"from": "2024-01-01", "to": "2024-01-31"},
        )
        assert page.data[0].bought_volume_usd == 50000.0


class TestDexTrades:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_dex_trades(self, respx_mock, client):
        respx_mock.post("/tgm/dex-trades").mock(
            return_value=_paginated_response([
                {
                    "trader_address": "0xabc",
                    "action": "BUY",
                    "estimated_value_usd": 25000.0,
                    "block_timestamp": "2024-01-01T00:00:00Z",
                    "transaction_hash": "0x123",
                }
            ])
        )
        page = client.tgm.dex_trades(
            chain="ethereum",
            token_address="0x0",
            date={"from": "2024-01-01", "to": "2024-01-31"},
        )
        assert page.data[0].action == "BUY"


class TestTransfers:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_transfers(self, respx_mock, client):
        respx_mock.post("/tgm/transfers").mock(
            return_value=_paginated_response([
                {
                    "from_address": "0xabc",
                    "to_address": "0xdef",
                    "transfer_value_usd": 100000.0,
                    "block_timestamp": "2024-01-01T00:00:00Z",
                    "transaction_hash": "0x123",
                }
            ])
        )
        page = client.tgm.transfers(
            chain="ethereum",
            token_address="0x0",
            date={"from": "2024-01-01", "to": "2024-01-31"},
        )
        assert page.data[0].transfer_value_usd == 100000.0


class TestDcas:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_dcas(self, respx_mock, client):
        respx_mock.post("/tgm/jup-dca").mock(
            return_value=_paginated_response([
                {
                    "trader_address": "abc123",
                    "token_input": "USDC",
                    "token_output": "SOL",
                    "status": "Active",
                    "deposit_usd_value": 10000.0,
                }
            ])
        )
        page = client.tgm.dcas(token_address="0x0")
        assert page.data[0].status == "Active"


class TestPnlLeaderboard:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_pnl_leaderboard(self, respx_mock, client):
        respx_mock.post("/tgm/pnl-leaderboard").mock(
            return_value=_paginated_response([
                {
                    "trader_address": "0xabc",
                    "pnl_usd_total": 100000.0,
                    "roi_percent_total": 500.0,
                }
            ])
        )
        page = client.tgm.pnl_leaderboard(
            chain="ethereum",
            token_address="0x0",
            date={"from": "2024-01-01", "to": "2024-01-31"},
        )
        assert page.data[0].pnl_usd_total == 100000.0


class TestPerpScreener:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_perp_screener(self, respx_mock, client):
        respx_mock.post("/perp-screener").mock(
            return_value=_paginated_response([
                {
                    "token_symbol": "BTC",
                    "volume": 100000000.0,
                    "mark_price": 50000.0,
                    "funding": 0.01,
                }
            ])
        )
        page = client.tgm.perp_screener(
            date={"from": "2024-01-01", "to": "2024-01-31"}
        )
        assert page.data[0].token_symbol == "BTC"


class TestPerpPnlLeaderboard:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_perp_pnl_leaderboard(self, respx_mock, client):
        respx_mock.post("/tgm/perp-pnl-leaderboard").mock(
            return_value=_paginated_response([
                {
                    "trader_address": "0xabc",
                    "pnl_usd_total": 50000.0,
                }
            ])
        )
        page = client.tgm.perp_pnl_leaderboard(
            token_symbol="BTC",
            date={"from": "2024-01-01", "to": "2024-01-31"},
        )
        assert page.data[0].pnl_usd_total == 50000.0


class TestPerpPositions:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_perp_positions(self, respx_mock, client):
        respx_mock.post("/tgm/perp-positions").mock(
            return_value=_paginated_response([
                {
                    "address": "0xabc",
                    "side": "Long",
                    "position_value_usd": 100000.0,
                    "leverage": "10x",
                    "entry_price": 50000.0,
                }
            ])
        )
        page = client.tgm.perp_positions(token_symbol="BTC")
        assert page.data[0].side == "Long"


class TestPerpTrades:
    @respx.mock(base_url="https://api.nansen.ai/api/v1")
    def test_perp_trades(self, respx_mock, client):
        respx_mock.post("/tgm/perp-trades").mock(
            return_value=_paginated_response([
                {
                    "trader_address": "0xabc",
                    "action": "Buy - Open Long",
                    "value_usd": 50000.0,
                    "type": "MARKET",
                    "block_timestamp": "2024-01-01T00:00:00Z",
                    "transaction_hash": "0x123",
                }
            ])
        )
        page = client.tgm.perp_trades(
            token_symbol="BTC",
            date={"from": "2024-01-01", "to": "2024-01-31"},
        )
        assert page.data[0].action == "Buy - Open Long"
