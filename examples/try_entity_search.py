"""Profiler — entity search — requires NANSEN_API_KEY env var.

Usage:
    export NANSEN_API_KEY="your-key"
    poetry run python examples/try_entity_search.py
"""

from nansen import APIError, Nansen, NansenError

client = Nansen()

try:
    resp = client.profiler.entity_search(search_query="Wintermute")

    entities = resp.data
    print(f"Got {len(entities)} matching entities\n")
    for entity in entities[:10]:
        print(f"  {entity.entity_name}")

except APIError as e:
    print(f"Error: {e}")
    print(f"Response body: {e.body}")
except NansenError as e:
    print(f"Error: {e}")
finally:
    client.close()
