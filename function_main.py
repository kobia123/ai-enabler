import json
import os
import time
import hashlib

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

        # =====================================
        # CACHE HIT
        # =====================================

        if os.path.exists(cache_file):

            cache_hit = True

            print("Loaded from cache")

            with open(
                cache_file,
                "r",
                encoding="utf-8"
            ) as cached:

                response_data = json.load(
                    cached
                )

            # New cache format
            if (
                isinstance(response_data, dict)
                and "result" in response_data
            ):

                insight = response_data["result"]

                usage = response_data.get(
                    "usage",
                    {}
                )

            # Legacy cache format
            else:

                insight = response_data

                usage = {
                    "input_tokens": None,
                    "output_tokens": None,
                    "total_tokens": None
                }

        # =====================================
        # CACHE MISS
        # =====================================

        else:

            print("Calling OpenAI...")

            response_data = analyze_function(
                function
            )

            insight = response_data["result"]

            usage = response_data["usage"]

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

        results.append(insight)

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

        # =====================================
        # EXECUTION LOG
        # =====================================

        log_entry = {
            "timestamp": datetime.now(
                UTC
            ).isoformat(),

            "function": function_name,

            "model": MODEL_NAME,

            "prompt_version": PROMPT_VERSION,

            "cache_hit": cache_hit,

            "execution_seconds": elapsed,

            "input_tokens": usage.get(
                "input_tokens"
            ),

            "output_tokens": usage.get(
                "output_tokens"
            ),

            "total_tokens": usage.get(
                "total_tokens"
            )
        }

        with open(
            "execution_log.jsonl",
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

        # =====================================
        # CHECKPOINT SAVE
        # =====================================

        with open(
            "function_insights_partial.json",
            "w",
            encoding="utf-8"
        ) as checkpoint:

            json.dump(
                {
                    "prompt_version":
                        PROMPT_VERSION,

                    "function_insights":
                        results
                },
                checkpoint,
                ensure_ascii=False,
                indent=2
            )

    except Exception as ex:

        print(
            f"ERROR processing "
            f"'{function_name}'"
        )

        print(ex)

# =========================================
# FINAL OUTPUT
# ===================