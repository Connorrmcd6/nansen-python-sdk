"""Smart Money holdings — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_smart_money.py
"""

from nansen import Nansen, NansenError

client = Nansen()  # reads NANSEN_API_KEY from env

try:
    page = client.smart_money.holdings(chains=["ethereum"])

    print(f"Got {len(page.data)} holdings on first page\n")
    for item in page.data[:10]:
        symbol = item.token_symbol or "???"
        value = f"${item.value_usd:,.2f}" if item.value_usd else "n/a"
        holders = item.holders_count or 0
        print(f"  {symbol:<12} value={value:<16} holders={holders}")

except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
