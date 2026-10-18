import json
import time

from roadmap_agent import (
    build_roadmap,
    MODEL_NAME
)

print(
    "Loading function insights..."
)

with open(
    "function_insights.json",
    "r",
    encoding="utf-8"
) as file:

    insights = json.load(file)

start_time = time.time()

roadmap = build_roadmap(
    insights
)

elapsed = round(
    time.time() - start_time,
    2
)

usage = roadmap.get(
    "usage",
    {}
)

print(
    f"Completed in {elapsed} seconds"
)

print(
    f"Input Tokens: "
    f"{usage.get('input_tokens')}"
)

print(
    f"Output Tokens: "
    f"{usage.get('output_tokens')}"
)

print(
    f"Total Tokens: "
    f"{usage.get('total_tokens')}"
)

with open(
    "ai_roadmap.json",
    "w",
    encoding="utf-8"
) as output:

    json.dump(
        roadmap["result"],
        output,
        ensure_ascii=False,
        indent=2
    )

print(
    "ai_roadmap.json created"
)