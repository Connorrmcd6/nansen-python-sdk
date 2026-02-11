"""Smart Money DCA orders — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_smart_money_dcas.py
"""

from nansen import APIError, Nansen, NansenError

client = Nansen()

try:
    page = client.smart_money.dcas()

    print(f"Got {len(page.data)} DCA orders\n")
    for dca in page.data[:10]:
        input_sym = dca.input_token_symbol or "???"
        output_sym = dca.output_token_symbol or "???"
        status = dca.dca_status or "?"
        deposit = f"${dca.deposit_value_usd:,.2f}" if dca.deposit_value_usd else "n/a"
        label = dca.trader_address_label or "unlabeled"
        print(f"  {label:<20} {input_sym}->{output_sym}  deposit={deposit}  status={status}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
