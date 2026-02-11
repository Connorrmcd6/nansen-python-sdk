"""Profiler — PnL summary & detailed PnL — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_profiler_pnl.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

# Vitalik's address
ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    # PnL summary
    summary_resp = client.profiler.pnl_summary(
        chain="ethereum",
        date=date,
        address=ADDRESS,
    )
    s = summary_resp.data
    if s:
        pnl = f"${s.realized_pnl_usd:,.2f}" if s.realized_pnl_usd else "n/a"
        win = f"{s.win_rate:.1f}%" if s.win_rate else "n/a"
        print(f"PnL Summary:")
        print(f"  Realized PnL: {pnl}")
        print(f"  Win rate: {win}")
        print(f"  Tokens traded: {s.traded_token_count or 0}")
        print(f"  Trades: {s.traded_times or 0}\n")

    # Detailed PnL
    page = client.profiler.pnl(
        chain="ethereum",
        address=ADDRESS,
    )

    print(f"Got {len(page.data)} PnL entries\n")
    for item in page.data[:10]:
        symbol = item.token_symbol or "???"
        pnl = f"${item.pnl_usd_realised:,.2f}" if item.pnl_usd_realised else "n/a"
        roi = f"{item.roi_percent_realised:.1f}%" if item.roi_percent_realised else "n/a"
        print(f"  {symbol:<12} pnl={pnl:<14} roi={roi}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
