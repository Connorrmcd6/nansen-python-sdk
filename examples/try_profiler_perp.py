"""Profiler — perp positions & trades — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_profiler_perp.py
"""

from datetime import datetime, timedelta, timezone

from nansen import Nansen, NansenError, APIError

# Example Hyperliquid trader address (replace with a known one)
ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

client = Nansen()

try:
    # Perp positions
    resp = client.profiler.perp_positions(address=ADDRESS)

    positions = resp.data
    if positions and positions.data and positions.data.assetPositions:
        print(f"Got {len(positions.data.assetPositions)} perp positions\n")
        for ap in positions.data.assetPositions[:10]:
            if ap.position:
                p = ap.position
                symbol = p.token_symbol or "???"
                value = p.position_value_usd or "n/a"
                entry = p.entry_price_usd or "n/a"
                pnl = p.unrealized_pnl_usd or "n/a"
                print(f"  {symbol:<8} value={value:<14} entry={entry:<12} upnl={pnl}")
    else:
        print("No perp positions found\n")

    # Perp trades
    now = datetime.now(timezone.utc)
    date = {
        "from": (now - timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    page = client.profiler.perp_trades(address=ADDRESS, date=date)

    print(f"\nGot {len(page.data)} perp trades\n")
    for trade in page.data[:10]:
        symbol = trade.token_symbol or "???"
        side = trade.side or "?"
        action = trade.action or "?"
        value = f"${trade.value_usd:,.2f}" if trade.value_usd else "n/a"
        print(f"  {symbol:<8} {side:<6} {action:<8} value={value}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
