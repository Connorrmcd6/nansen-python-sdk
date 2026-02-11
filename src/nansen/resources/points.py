from __future__ import annotations

from pydantic import TypeAdapter

from nansen._constants import POINTS_BASE_URL
from nansen._response import APIResponse
from nansen._types import NOT_GIVEN, NotGiven, _NotGiven
from nansen.resources._base import AsyncAPIResource, SyncAPIResource
from nansen.types.points import PointsLeaderboardEntry


class Points(SyncAPIResource):
    def leaderboard(
        self,
        *,
        tier: str | NotGiven = NOT_GIVEN,
    ) -> APIResponse[list[PointsLeaderboardEntry]]:
        """Fetch the points leaderboard.

        This endpoint uses GET, requires no authentication,
        and hits a different base URL (app.nansen.ai).
        """
        params = {}
        if not isinstance(tier, _NotGiven):
            params["tier"] = tier

        response = self._client._request(
            "GET",
            "/api/points-leaderboard",
            params=params or None,
            headers={"content-type": "application/json"},
            base_url=POINTS_BASE_URL,
        )
        items = TypeAdapter(list[PointsLeaderboardEntry]).validate_python(response.json())
        return APIResponse(data=items, http_response=response)


class AsyncPoints(AsyncAPIResource):
    async def leaderboard(
        self,
        *,
        tier: str | NotGiven = NOT_GIVEN,
    ) -> APIResponse[list[PointsLeaderboardEntry]]:
        """Fetch the points leaderboard (async)."""
        params = {}
        if not isinstance(tier, _NotGiven):
            params["tier"] = tier

        response = await self._client._request(
            "GET",
            "/api/points-leaderboard",
            params=params or None,
            headers={"content-type": "application/json"},
            base_url=POINTS_BASE_URL,
        )
        items = TypeAdapter(list[PointsLeaderboardEntry]).validate_python(response.json())
        return APIResponse(data=items, http_response=response)
