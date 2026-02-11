"""Smart Money netflow — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_smart_money_netflow.py
"""

from nansen import Nansen, NansenError, APIError

client = Nansen()

try:
    page = client.smart_money.netflow(chains=["ethereum"])

    print(f"Got {len(page.data)} netflow entries\n")
    for item in page.data[:10]:
        symbol = item.token_symbol or "???"
        net_24h = f"${item.net_flow_24h_usd:,.0f}" if item.net_flow_24h_usd else "n/a"
        traders = item.trader_count or 0
        print(f"  {symbol:<12} 24h_net={net_24h:<16} traders={traders}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
