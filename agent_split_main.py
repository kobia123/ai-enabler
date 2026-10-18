import json
import time

from datetime import datetime, UTC

from function_analysis import (
    analyze_function,
    MODEL_NAME
)

from ai_opportunity_agent import (
    discover_opportunities
)

print(
    "Loading organization profile..."
)

with open(
    "organization_profile.json",
    "r",
    encoding="utf-8"
) as file:

    profile = json.load(file)

functions = profile.get(
    "business_functions",
    []
)

print(
    f"Found {len(functions)} business functions"
)

results = []

for function in functions:

    function_name = function.get(
        "name",
        "Unknown Function"
    )

    print(
        f"\nProcessing: {function_name}"
    )

    # ====================================
    # Agent A
    # ====================================

    start_a = time.time()

    analysis = analyze_function(
        function
    )

    elapsed_a = round(
        time.time() - start_a,
        2
    )

    analysis_usage = analysis.get(
        "usage",
        {}
    )

    print("\n=== AGENT A ===")

    print(
        f"Time: {elapsed_a} sec"
    )

    print(
        f"Input Tokens: "
        f"{analysis_usage.get('input_tokens')}"
    )

    print(
        f"Output Tokens: "
        f"{analysis_usage.get('output_tokens')}"
    )

    print(
        f"Total Tokens: "
        f"{analysis_usage.get('total_tokens')}"
    )

    # ====================================
    # Agent B
    # ====================================

    start_b = time.time()

    opportunities = (
        discover_opportunities(
            analysis["result"]
        )
    )

    elapsed_b = round(
        time.time() - start_b,
        2
    )

    opportunity_usage = (
        opportunities.get(
            "usage",
            {}
        )
    )

    print("\n=== AGENT B ===")

    print(
        f"Time: {elapsed_b} sec"
    )

    print(
        f"Input Tokens: "
        f"{opportunity_usage.get('input_tokens')}"
    )

    print(
        f"Output Tokens: "
        f"{opportunity_usage.get('output_tokens')}"
    )

    print(
        f"Total Tokens: "
        f"{opportunity_usage.get('total_tokens')}"
    )

    # ====================================
    # Totals
    # ====================================

    total_time = round(
        elapsed_a + elapsed_b,
        2
    )

    total_tokens = (
        (
            analysis_usage.get(
                "total_tokens"
            ) or 0
        )
        +
        (
            opportunity_usage.get(
                "total_tokens"
            ) or 0
        )
    )

    print("\n=== TOTAL ===")

    print(
        f"Total Time: "
        f"{total_time} sec"
    )

    print(
        f"Total Tokens: "
        f"{total_tokens}"
    )

    # ====================================
    # Log Entry
    # ====================================

    log_entry = {

        "timestamp":
            datetime.now(
                UTC
            ).isoformat(),

        "function":
            function_name,

        "model":
            MODEL_NAME,

        "agent_a_time":
            elapsed_a,

        "agent_b_time":
            elapsed_b,

        "total_time":
            total_time,

        "agent_a_input_tokens":
            analysis_usage.get(
                "input_tokens"
            ),

        "agent_a_output_tokens":
            analysis_usage.get(
                "output_tokens"
            ),

        "agent_a_total_tokens":
            analysis_usage.get(
                "total_tokens"
            ),

        "agent_b_input_tokens":
            opportunity_usage.get(
                "input_tokens"
            ),

        "agent_b_output_tokens":
            opportunity_usage.get(
                "output_tokens"
            ),

        "agent_b_total_tokens":
            opportunity_usage.get(
                "total_tokens"
            ),

        "total_tokens":
            total_tokens
    }

    with open(
        "agent_split_log.jsonl",
        "a",
        encoding="utf-8"
    ) as log:

        log.write(
            json.dumps(
                log_entry,
                ensure_ascii=False
            )
            + "\n"
        )

    results.append(
        {
            "function_name":
                function_name,

            "analysis":
                analysis["result"],

            "ai_opportunities":
                opportunities[
                    "result"
                ][
                    "ai_opportunities"
                ]
        }
    )

# ====================================
# Final Output
# ====================================

final_result = {
    "function_insights":
        results
}

with open(
    "function_ai_opportunities.json",
    "w",
    encoding="utf-8"
) as output:

    json.dump(
        final_result,
        output,
        ensure_ascii=False,
        indent=2
    )

print(
    "\nfunction_ai_opportunities.json created"
)