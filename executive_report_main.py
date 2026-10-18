import json
import time

from executive_report_agent import (
    create_executive_report
)

print(
    "Loading AI roadmap..."
)

with open(
    "ai_roadmap.json",
    "r",
    encoding="utf-8"
) as file:

    roadmap = json.load(
        file
    )

start_time = time.time()

report = (
    create_executive_report(
        roadmap
    )
)

elapsed = round(
    time.time() - start_time,
    2
)

usage = report.get(
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
    "executive_report.json",
    "w",
    encoding="utf-8"
) as output:

    json.dump(
        report["result"],
        output,
        ensure_ascii=False,
        indent=2
    )

print(
    "executive_report.json created"
)