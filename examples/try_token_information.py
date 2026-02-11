"""Token God Mode — token information — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_token_information.py
"""

from nansen import APIError, Nansen, NansenError

# PEPE on Ethereum
TOKEN_ADDRESS = "0x6982508145454Ce325dDbE47a25d4ec3d2311933"

client = Nansen()

try:
    resp = client.tgm.token_information(
        chain="ethereum",
        token_address=TOKEN_ADDRESS,
        timeframe="24h",
    )

    info = resp.data
    if info and info.data:
        d = info.data
        print(f"Token: {d.name} ({d.symbol})")
        print(f"Address: {d.contract_address}")
        if d.token_details:
            td = d.token_details
            mcap = f"${td.market_cap_usd:,.0f}" if td.market_cap_usd else "n/a"
            fdv = f"${td.fdv_usd:,.0f}" if td.fdv_usd else "n/a"
            print(f"Market cap: {mcap}")
            print(f"FDV: {fdv}")
        if d.spot_metrics:
            sm = d.spot_metrics
            vol = f"${sm.volume_total_usd:,.0f}" if sm.volume_total_usd else "n/a"
            liq = f"${sm.liquidity_usd:,.0f}" if sm.liquidity_usd else "n/a"
            print(f"Volume: {vol}")
            print(f"Liquidity: {liq}")
    else:
        print("No data returned")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
