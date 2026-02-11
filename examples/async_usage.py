"""Async usage of the Nansen Python SDK."""

import asyncio

from nansen import AsyncNansen


async def main():
    async with AsyncNansen(api_key="your-api-key") as client:
        # Smart Money holdings — async auto-pagination
        page = await client.smart_money.holdings(chains=["ethereum"])
        async for item in page:
            print(f"{item.token_symbol}: ${item.value_usd}")

        # Token information
        resp = await client.tgm.token_information(
            chain="ethereum",
            token_address="0x6982508145454ce325ddbe47a25d4ec3d2311933",
            timeframe="24h",
        )
        info = resp.data.data
        print(f"{info.name} ({info.symbol})")
        if info.token_details:
            print(f"  Market cap: ${info.token_details.market_cap_usd:,.0f}")
        if info.spot_metrics:
            print(f"  24h volume: ${info.spot_metrics.volume_total_usd:,.0f}")

        # Points leaderboard (no auth needed)
        points = await client.points.leaderboard(tier="star")
        for entry in points.data[:5]:
            print(f"  #{entry.rank} {entry.evm_address}: {entry.points} pts")


asyncio.run(main())
