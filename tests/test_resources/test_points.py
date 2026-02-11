import httpx
import pytest
import respx

from nansen import Nansen


@pytest.fixture
def client():
    with Nansen(api_key="test-key") as c:
        yield c


class TestPointsLeaderboard:
    @respx.mock(base_url="https://app.nansen.ai")
    def test_leaderboard(self, respx_mock, client):
        respx_mock.get("/api/points-leaderboard").mock(
            return_value=httpx.Response(
                200,
                json=[
                    {
                        "rank": 1,
                        "evm_address": "0xabc",
                        "solana_address": None,
                        "points": 50000,
                        "tier": "star",
                        "is_eligible": True,
                    },
                    {
                        "rank": 2,
                        "evm_address": "0xdef",
                        "solana_address": "sol123",
                        "points": 40000,
                        "tier": "north",
                        "is_eligible": True,
                    },
                ],
            )
        )
        resp = client.points.leaderboard()
        assert len(resp.data) == 2
        assert resp.data[0].rank == 1
        assert resp.data[0].tier == "star"
        assert resp.data[1].solana_address == "sol123"

    @respx.mock(base_url="https://app.nansen.ai")
    def test_leaderboard_with_tier(self, respx_mock, client):
        route = respx_mock.get("/api/points-leaderboard").mock(
            return_value=httpx.Response(200, json=[])
        )
        client.points.leaderboard(tier="green")
        assert route.calls[0].request.url.params["tier"] == "green"
