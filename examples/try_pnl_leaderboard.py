"""Token God Mode — PnL leaderboard — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_pnl_leaderboard.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

# PEPE on Ethereum
TOKEN_ADDRESS = "0x6982508145454Ce325dDbE47a25d4ec3d2311933"

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.tgm.pnl_leaderboard(
        chain="ethereum",
        token_address=TOKEN_ADDRESS,
        date=date,
    )

    print(f"Got {len(page.data)} leaderboard entries\n")
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
