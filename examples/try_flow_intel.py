"""Token God Mode — flow intelligence — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_flow_intel.py
"""

from nansen import APIError, Nansen, NansenError

# PEPE on Ethereum
TOKEN_ADDRESS = "0x6982508145454Ce325dDbE47a25d4ec3d2311933"

client = Nansen()

try:
    page = client.tgm.flow_intel(
        chain="ethereum",
        token_address=TOKEN_ADDRESS,
        timeframe="24h",
    )

    print(f"Got {len(page.data)} flow intel entries\n")
    for item in page.data[:5]:

        def fmt(v):
            return f"${v:,.0f}" if v else "n/a"

        print("  Smart Traders:")
        print(
            f"    net_flow={fmt(item.smart_trader_net_flow_usd)}"
            f"  wallets={item.smart_trader_wallet_count}"
        )
        print("  Whales:")
        print(f"    net_flow={fmt(item.whale_net_flow_usd)}  wallets={item.whale_wallet_count}")
        print("  Exchanges:")
        print(
            f"    net_flow={fmt(item.exchange_net_flow_usd)}  wallets={item.exchange_wallet_count}"
        )
        print("  Fresh Wallets:")
        print(
            f"    net_flow={fmt(item.fresh_wallets_net_flow_usd)}"
            f"  wallets={item.fresh_wallets_wallet_count}"
        )

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
