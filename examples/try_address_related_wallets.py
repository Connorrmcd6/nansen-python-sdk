"""Profiler — address related wallets — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_address_related_wallets.py
"""

from nansen import APIError, Nansen, NansenError

# Vitalik's address
ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    page = client.profiler.address.related_wallets(
        address=ADDRESS,
        chain="ethereum",
    )

    print(f"Got {len(page.data)} related wallets\n")
    for wallet in page.data[:10]:
        addr = wallet.address or "???"
        label = wallet.address_label or "unlabeled"
        relation = wallet.relation or "?"
        chain = wallet.chain or "?"
        print(f"  {label:<25} relation={relation:<12} chain={chain}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
