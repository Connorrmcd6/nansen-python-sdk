"""Token God Mode — flows — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_flows.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

# PEPE on Ethereum
TOKEN_ADDRESS = "0x6982508145454Ce325dDbE47a25d4ec3d2311933"

client = Nansen()

try:
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.tgm.flows(
        chain="ethereum",
        token_address=TOKEN_ADDRESS,
        date=date,
    )

    print(f"Got {len(page.data)} flow entries\n")
    for flow in page.data[:10]:
        d = flow.date or "?"
        price = f"${flow.price_usd:,.6f}" if flow.price_usd else "n/a"
        value = f"${flow.value_usd:,.0f}" if flow.value_usd else "n/a"
        holders = flow.holders_count or 0
        print(f"  {d[:10]}  price={price:<16} value={value:<14} holders={holders}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
