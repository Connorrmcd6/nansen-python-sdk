"""Token God Mode — perp positions — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_tgm_perp_positions.py
"""

from nansen import APIError, Nansen, NansenError

client = Nansen()

try:
    page = client.tgm.perp_positions(token_symbol="BTC")

    print(f"Got {len(page.data)} perp positions\n")
    for pos in page.data[:10]:
        label = pos.address_label or pos.address or "???"
        side = pos.side or "?"
        value = f"${pos.position_value_usd:,.0f}" if pos.position_value_usd else "n/a"
        entry = f"${pos.entry_price:,.2f}" if pos.entry_price else "n/a"
        leverage = pos.leverage or "?"
        print(f"  {label:<25} {side:<6} value={value:<14} entry={entry:<12} leverage={leverage}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
