"""Token God Mode — holders — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_holders.py
"""

from nansen import Nansen, NansenError, APIError

# PEPE on Ethereum
TOKEN_ADDRESS = "0x6982508145454Ce325dDbE47a25d4ec3d2311933"

client = Nansen()

try:
    page = client.tgm.holders(
        chain="ethereum",
        token_address=TOKEN_ADDRESS,
    )

    print(f"Got {len(page.data)} holders\n")
    for holder in page.data[:10]:
        label = holder.address_label or holder.address or "???"
        value = f"${holder.value_usd:,.0f}" if holder.value_usd else "n/a"
        pct = f"{holder.ownership_percentage:.2f}%" if holder.ownership_percentage else "n/a"
        print(f"  {label:<30} value={value:<16} ownership={pct}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
