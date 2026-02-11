"""Profiler — perp leaderboard — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_perp_leaderboard.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.profiler.perp_leaderboard(date=date)

    print(f"Got {len(page.data)} perp leaderboard entries\n")
    for item in page.data[:10]:
        label = item.trader_address_label or item.trader_address or "???"
        pnl = f"${item.total_pnl:,.0f}" if item.total_pnl else "n/a"
        roi = f"{item.roi:.1f}%" if item.roi else "n/a"
        acct = f"${item.account_value:,.0f}" if item.account_value else "n/a"
        print(f"  {label:<30} pnl={pnl:<14} roi={roi:<10} acct={acct}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
