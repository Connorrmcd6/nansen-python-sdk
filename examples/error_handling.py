"""Error handling with the Nansen Python SDK."""

from nansen import (
    AuthenticationError,
    Nansen,
    NansenError,
    RateLimitError,
)

client = Nansen(api_key="your-api-key")

try:
    page = client.smart_money.holdings(chains=["ethereum"])
    for item in page:
        print(f"{item.token_symbol}: ${item.value_usd}")
except AuthenticationError:
    print("Invalid API key. Check your NANSEN_API_KEY.")
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
    print(f"Credits remaining: {e.response.headers.get('x-nansen-credits-remaining')}")
except NansenError as e:
    print(f"API error: {e}")
finally:
    client.close()
