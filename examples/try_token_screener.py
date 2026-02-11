"""Token God Mode screener — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_token_screener.py
"""

from nansen import APIError, Nansen, NansenError

client = Nansen()  # reads NANSEN_API_KEY from env

try:
    page = client.tgm.token_screener(chains=["ethereum"], timeframe="24h")

    print(f"Got {len(page.data)} tokens on first page\n")
    for token in page.data[:10]:
        symbol = token.token_symbol or "???"
        price = f"${token.price_usd:,.4f}" if token.price_usd else "n/a"
        mcap = f"${token.market_cap_usd:,.0f}" if token.market_cap_usd else "n/a"
        print(f"  {symbol:<12} price={price:<16} mcap={mcap}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
