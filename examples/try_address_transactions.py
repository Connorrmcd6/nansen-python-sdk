"""Profiler — address transactions — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_address_transactions.py
"""

from datetime import datetime, timedelta, timezone

from nansen import APIError, Nansen, NansenError

# Vitalik's address
ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.profiler.address.transactions(
        address=ADDRESS,
        chain="ethereum",
        date=date,
    )

    print(f"Got {len(page.data)} transactions\n")
    for tx in page.data[:10]:
        method = tx.method or "?"
        ts = tx.block_timestamp or "?"
        vol = f"${tx.volume_usd:,.2f}" if tx.volume_usd else "n/a"
        src = tx.source_type or "?"
        print(f"  {ts[:19]}  {method:<20} volume={vol:<14} source={src}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
