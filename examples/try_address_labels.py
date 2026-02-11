"""Profiler — address labels (beta) — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_address_labels.py
"""

from nansen import Nansen, NansenError, APIError

# Vitalik's address
ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    resp = client.profiler.address.labels(
        chain="ethereum",
        address=ADDRESS,
    )

    labels = resp.data
    print(f"Got {len(labels)} labels\n")
    for item in labels[:10]:
        label = item.label or "???"
        category = item.category or "?"
        definition = item.definition or ""
        print(f"  {label:<25} category={category:<15} {definition}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
