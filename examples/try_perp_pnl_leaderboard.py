"""Token God Mode — perp PnL leaderboard — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_perp_pnl_leaderboard.py
"""

from datetime import datetime, timedelta, timezone

from nansen import APIError, Nansen, NansenError

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.tgm.perp_pnl_leaderboard(
        token_symbol="BTC",
        date=date,
    )

    print(f"Got {len(page.data)} perp PnL leaderboard entries\n")
    for item in page.data[:10]:
        label = item.trader_address_label or item.trader_address or "???"
        pnl = f"${item.pnl_usd_total:,.0f}" if item.pnl_usd_total else "n/a"
        roi = f"{item.roi_percent_total:.1f}%" if item.roi_percent_total else "n/a"
        trades = item.nof_trades or 0
        print(f"  {label:<30} pnl={pnl:<14} roi={roi:<10} trades={trades}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
