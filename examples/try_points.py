"""Points leaderboard — no API key needed."""

from nansen import Nansen

client = Nansen(api_key="unused")

resp = client.points.leaderboard()

print(f"Got {len(resp.data)} leaderboard entries\n")
for entry in resp.data[:10]:
    print(
        f"  #{entry.rank}  "
        f"tier={entry.tier}  "
        f"points={entry.points}  "
        f"evm={entry.evm_address}"
    )

client.close()
