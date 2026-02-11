"""Token God Mode — Jupiter DCA orders — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_tgm_dcas.py
"""

from nansen import APIError, Nansen, NansenError

# JUP token on Solana
TOKEN_ADDRESS = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"

client = Nansen()

try:
    page = client.tgm.dcas(token_address=TOKEN_ADDRESS)

    print(f"Got {len(page.data)} DCA orders\n")
    for dca in page.data[:10]:
        input_sym = dca.token_input or "???"
        output_sym = dca.token_output or "???"
        status = dca.status or "?"
        deposit = f"${dca.deposit_usd_value:,.2f}" if dca.deposit_usd_value else "n/a"
        label = dca.trader_label or "unlabeled"
        print(f"  {label:<20} {input_sym}->{output_sym}  deposit={deposit}  status={status}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
