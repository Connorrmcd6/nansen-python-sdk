"""Smart Money historical holdings — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_smart_money_historical_holdings.py
"""

from datetime import datetime, timedelta, timezone

from nansen import APIError, Nansen, NansenError

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date_range = {
        "from": (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.smart_money.historical_holdings(
        date_range=date_range,
        chains=["ethereum"],
    )

    print(f"Got {len(page.data)} historical holding entries\n")
    for item in page.data[:10]:
        symbol = item.token_symbol or "???"
        date = item.date or "?"
        value = f"${item.value_usd:,.2f}" if item.value_usd else "n/a"
        holders = item.holders_count or 0
        print(f"  {date[:10]}  {symbol:<12} value={value:<16} holders={holders}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
