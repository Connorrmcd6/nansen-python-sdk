"""Profiler — address current balance — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_address_balance.py
"""

from nansen import Nansen, NansenError, APIError

# Vitalik's address
ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    page = client.profiler.address.current_balance(
        chain="ethereum",
        address=ADDRESS,
    )

    print(f"Got {len(page.data)} token balances\n")
    for item in page.data[:10]:
        symbol = item.token_symbol or "???"
        name = item.token_name or ""
        value = f"${item.value_usd:,.2f}" if item.value_usd else "n/a"
        amount = f"{item.token_amount:,.4f}" if item.token_amount else "n/a"
        print(f"  {symbol:<10} {name:<20} amount={amount:<18} value={value}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
