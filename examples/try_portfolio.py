"""Portfolio DeFi holdings — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_portfolio.py
"""

from nansen import Nansen, NansenError, APIError

# Vitalik's address
WALLET_ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    resp = client.portfolio.defi_holdings(wallet_address=WALLET_ADDRESS)

    holdings = resp.data
    if holdings and holdings.summary:
        s = holdings.summary
        total = f"${s.total_value_usd:,.2f}" if s.total_value_usd else "n/a"
        print(f"Total DeFi value: {total}")
        print(f"Protocols: {s.protocol_count or 0}  Tokens: {s.token_count or 0}\n")

    if holdings and holdings.protocols:
        for proto in holdings.protocols[:10]:
            name = proto.protocol_name or "???"
            chain = proto.chain or "?"
            value = f"${proto.total_value_usd:,.2f}" if proto.total_value_usd else "n/a"
            print(f"  {name:<20} chain={chain:<12} value={value}")
    else:
        print("No protocol holdings found")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
