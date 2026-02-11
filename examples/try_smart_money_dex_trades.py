"""Smart Money DEX trades — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_smart_money_dex_trades.py
"""

from nansen import APIError, Nansen, NansenError

client = Nansen()

try:
    page = client.smart_money.dex_trades(chains=["ethereum"])

    print(f"Got {len(page.data)} DEX trades\n")
    for trade in page.data[:10]:
        bought = trade.token_bought_symbol or "???"
        sold = trade.token_sold_symbol or "???"
        value = f"${trade.trade_value_usd:,.2f}" if trade.trade_value_usd else "n/a"
        label = trade.trader_address_label or "unlabeled"
        print(f"  {label:<20} {sold} -> {bought}  value={value}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
