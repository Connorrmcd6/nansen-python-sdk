"""Token God Mode — perp trades — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_tgm_perp_trades.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.tgm.perp_trades(
        token_symbol="BTC",
        date=date,
    )

    print(f"Got {len(page.data)} perp trades\n")
    for trade in page.data[:10]:
        label = trade.trader_address_label or "unlabeled"
        side = trade.side or "?"
        action = trade.action or "?"
        value = f"${trade.value_usd:,.2f}" if trade.value_usd else "n/a"
        ts = trade.block_timestamp or ""
        print(f"  {ts[:19]}  {label:<20} {side:<6} {action:<8} value={value}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
