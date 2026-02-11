"""Profiler — address historical balances — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_address_historical_balances.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

# Vitalik's address
ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.profiler.address.historical_balances(
        chain="ethereum",
        date=date,
        address=ADDRESS,
    )

    print(f"Got {len(page.data)} historical balance entries\n")
    for item in page.data[:10]:
        symbol = item.token_symbol or "???"
        ts = item.block_timestamp or "?"
        value = f"${item.value_usd:,.2f}" if item.value_usd else "n/a"
        amount = f"{item.token_amount:,.4f}" if item.token_amount else "n/a"
        print(f"  {ts[:10]}  {symbol:<10} amount={amount:<18} value={value}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
