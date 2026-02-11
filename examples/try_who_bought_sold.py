"""Token God Mode — who bought/sold — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_who_bought_sold.py
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

    page = client.tgm.who_bought_sold(
        chain="ethereum",
        token_address=TOKEN_ADDRESS,
        date=date,
    )

    print(f"Got {len(page.data)} buyer/seller entries\n")
    for item in page.data[:10]:
        label = item.address_label or item.address or "???"
        bought = f"${item.bought_volume_usd:,.0f}" if item.bought_volume_usd else "n/a"
        sold = f"${item.sold_volume_usd:,.0f}" if item.sold_volume_usd else "n/a"
        print(f"  {label:<30} bought={bought:<14} sold={sold}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
