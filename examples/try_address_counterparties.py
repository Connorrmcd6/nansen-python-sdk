"""Profiler — address counterparties — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_address_counterparties.py
"""

from datetime import datetime, timedelta, timezone

from nansen import APIError, Nansen, NansenError

# Vitalik's address
ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.profiler.address.counterparties(
        chain="ethereum",
        date=date,
        address=ADDRESS,
    )

    print(f"Got {len(page.data)} counterparties\n")
    for cp in page.data[:10]:
        addr = cp.counterparty_address or "???"
        labels = (
            ", ".join(cp.counterparty_address_label)
            if cp.counterparty_address_label
            else "unlabeled"
        )
        vol = f"${cp.total_volume_usd:,.0f}" if cp.total_volume_usd else "n/a"
        count = cp.interaction_count or 0
        print(f"  {labels:<30} interactions={count:<6} volume={vol}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
