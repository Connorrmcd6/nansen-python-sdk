"""Smart Money perp trades — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_smart_money_perp_trades.py
"""

from nansen import Nansen, NansenError, APIError

client = Nansen()

try:
    page = client.smart_money.perp_trades()

    print(f"Got {len(page.data)} perp trades\n")
    for trade in page.data[:10]:
        symbol = trade.token_symbol or "???"
        side = trade.side or "?"
        action = trade.action or "?"
        value = f"${trade.value_usd:,.2f}" if trade.value_usd else "n/a"
        label = trade.trader_address_label or "unlabeled"
        print(f"  {label:<20} {symbol:<8} {side:<6} {action:<8} value={value}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
