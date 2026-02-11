"""Token God Mode — perp screener — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_perp_screener.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.tgm.perp_screener(date=date)

    print(f"Got {len(page.data)} perp tokens\n")
    for item in page.data[:10]:
        symbol = item.token_symbol or "???"
        vol = f"${item.volume:,.0f}" if item.volume else "n/a"
        funding = f"{item.funding:.4f}" if item.funding else "n/a"
        oi = f"${item.open_interest:,.0f}" if item.open_interest else "n/a"
        print(f"  {symbol:<8} volume={vol:<16} funding={funding:<12} OI={oi}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
