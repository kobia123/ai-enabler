import json

import httpx
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL_NAME = "gpt-6.1-sol"

client = OpenAI(
    http_client=httpx.Client(
        verify=False,
        timeout=300
    )
)

SYSTEM_PROMPT = """
You are a senior AI strategist,
enterprise architect,
transformation consultant
and CIO advisor.

You are given AI opportunities
identified across one or more
business functions.

Your task is to create
an enterprise AI roadmap.

Review all opportunities.

Prioritize initiatives according to:

- business value
- impact score
- complexity score
- data readiness
- organizational benefit

Do NOT create new opportunities.

Use only opportunities that already exist.

Organize initiatives into:

1. Quick Wins
   0-6 months

2. Mid-Term Initiatives
   6-12 months

3. Strategic Initiatives
   12-24 months

Keep recommendations concise.

Executive Summary:
- maximum 5 sentences

Reason:
- maximum 2 sentences

Return VALID JSON ONLY.

Schema:

{
  "executive_summary": "",

  "quick_wins": [
    {
      "initiative": "",
      "business_function": "",
      "reason": ""
    }
  ],

  "mid_term": [
    {
      "initiative": "",
      "business_function": "",
      "reason": ""
    }
  ],

  "strategic": [
    {
      "initiative": "",
      "business_function": "",
      "reason": ""
    }
  ]
}

Do not return markdown.
Do not wrap JSON in code fences.
Do not return explanations.
"""


def build_roadmap(insights):

    compact_insights = []

    for function in insights.get(
        "function_insights",
        []
    ):

        compact_insights.append(
            {
                "business_function":
                    function.get(
                        "name",
                        ""
                    ),

                "opportunities":
                    function.get(
                        "ai_opportunities",
                        []
                    )
            }
        )

    response = client.responses.create(
        model=MODEL_NAME,
        input=f"""
{SYSTEM_PROMPT}

FUNCTION INSIGHTS:

{json.dumps(
    compact_insights,
    ensure_ascii=False,
    indent=2
)}
"""
    )

    raw_response = (
        response.output_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    result = json.loads(
        raw_response
    )

    usage = {
        "input_tokens": None,
        "output_tokens": None,
        "total_tokens": None
    }

    try:

        usage["input_tokens"] = (
            response.usage.input_tokens
        )

        usage["output_tokens"] = (
            response.usage.output_tokens
        )

        usage["total_tokens"] = (
            response.usage.total_tokens
        )

    except Exception:
        pass

    return {
        "result": result,
        "usage": usage
    }