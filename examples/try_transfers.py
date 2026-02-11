"""Token God Mode — transfers — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_transfers.py
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

    page = client.tgm.transfers(
        chain="ethereum",
        token_address=TOKEN_ADDRESS,
        date=date,
    )

    print(f"Got {len(page.data)} transfers\n")
    for t in page.data[:10]:
        from_label = t.from_address_label or t.from_address or "???"
        to_label = t.to_address_label or t.to_address or "???"
        value = f"${t.transfer_value_usd:,.2f}" if t.transfer_value_usd else "n/a"
        tx_type = t.transaction_type or "?"
        print(f"  {from_label[:20]:<20} -> {to_label[:20]:<20}  {tx_type:<10} value={value}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
