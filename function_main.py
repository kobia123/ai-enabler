import json
import os
import time
import hashlib
import traceback

from datetime import datetime, UTC

from function_insight import (
    analyze_function,
    PROMPT_VERSION,
    MODEL_NAME
)

CACHE_DIR = "cache"

os.makedirs(
    CACHE_DIR,
    exist_ok=True
)

print("Loading organization profile...")

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

for index, function in enumerate(
    functions,
    start=1
):

    function_name = function.get(
        "name",
        f"function_{index}"
    )

    print(
        f"\n[{index}/{len(functions)}] "
        f"Processing: {function_name}"
    )

    cache_key_source = (
        PROMPT_VERSION +
        json.dumps(
            function,
            ensure_ascii=False,
            sort_keys=True
        )
    )

    function_hash = hashlib.md5(
        cache_key_source.encode("utf-8")
    ).hexdigest()

    cache_file = os.path.join(
        CACHE_DIR,
        f"{function_hash}.json"
    )

    cache_hit = False

    start_time = time.time()

    try:

        if os.path.exists(cache_file):

            cache_hit = True

            print(
                "Loaded from cache"
            )

            with open(
                cache_file,
                "r",
                encoding="utf-8"
            ) as cached:

                response_data = json.load(
                    cached
                )

            if (
                isinstance(response_data, dict)
                and "result" in response_data
            ):

                insight = (
                    response_data[
                        "result"
                    ]
                )

                usage = (
                    response_data.get(
                        "usage",
                        {}
                    )
                )

            else:

                insight = response_data

                usage = {
                    "input_tokens": None,
                    "output_tokens": None,
                    "total_tokens": None
                }

        else:

            print(
                "Calling OpenAI..."
            )

            response_data = (
                analyze_function(
                    function
                )
            )

            print(
                "OpenAI response received"
            )

            insight = (
                response_data[
                    "result"
                ]
            )

            usage = (
                response_data[
                    "usage"
                ]
            )

            with open(
                cache_file,
                "w",
                encoding="utf-8"
            ) as cached:

                json.dump(
                    response_data,
                    cached,
                    ensure_ascii=False,
                    indent=2
                )

        results.append(
            insight
        )

        elapsed = round(
            time.time() - start_time,
            2
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

    except Exception:

        print(
            f"\nERROR processing "
            f"'{function_name}'"
        )

        print(
            "\n===== FULL ERROR =====\n"
        )

        traceback.print_exc()

        print(
            "\n===== END ERROR =====\n"
        )

# =====================================
# FINAL OUTPUT
# =====================================

print(
    "\nSaving final output..."
)

final_output = {
    "prompt_version":
        PROMPT_VERSION,

    "function_insights":
        results
}

with open(
    "function_insights.json",
    "w",
    encoding="utf-8"
) as output:

    json.dump(
        final_output,
        output,
        ensure_ascii=False,
        indent=2
    )

print(
    f"function_insights.json "
    f"created with "
    f"{len(results)} functions"
)

print(
    f"Prompt Version: "
    f"{PROMPT_VERSION}"
)