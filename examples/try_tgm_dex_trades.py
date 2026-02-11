"""Token God Mode — DEX trades — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_tgm_dex_trades.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

# PEPE on Ethereum
TOKEN_ADDRESS = "0x6982508145454Ce325dDbE47a25d4ec3d2311933"

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.tgm.dex_trades(
        chain="ethereum",
        token_address=TOKEN_ADDRESS,
        date=date,
    )

    print(f"Got {len(page.data)} DEX trades\n")
    for trade in page.data[:10]:
        action = trade.action or "?"
        label = trade.trader_address_label or "unlabeled"
        value = f"${trade.estimated_value_usd:,.2f}" if trade.estimated_value_usd else "n/a"
        ts = trade.block_timestamp or ""
        print(f"  {ts[:19]}  {label:<20} {action:<6} value={value}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
