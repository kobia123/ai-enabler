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
You are a senior executive advisor,
CIO strategist,
enterprise architect,
and AI transformation consultant.

You are given an AI roadmap.

Create an executive-level report.

Audience:

- CEO
- Executive Leadership
- CIO
- Board Members

The report should be concise,
business-oriented,
and non-technical.

Include:

1. Executive Summary
2. Organizational AI Readiness
3. Top Quick Wins
4. Top Strategic Initiatives
5. Expected Business Benefits
6. Key Risks
7. Recommended Next Steps

Keep the report concise.

Executive Summary:
- maximum 3 sentences

Top Quick Wins:
- maximum 3 items

Top Strategic Initiatives:
- maximum 3 items

Expected Business Benefits:
- maximum 5 items

Key Risks:
- maximum 5 items

Recommended Next Steps:
- maximum 5 items

Return VALID JSON ONLY.

Schema:

{
  "executive_summary": "",

  "ai_readiness": {
    "level": "",
    "reason": ""
  },

  "top_quick_wins": [
    ""
  ],

  "top_strategic_initiatives": [
    ""
  ],

  "expected_business_benefits": [
    ""
  ],

  "key_risks": [
    ""
  ],

  "recommended_next_steps": [
    ""
  ]
}

Return JSON only.
Do not return markdown.
Do not return explanations.
"""


def create_executive_report(roadmap):

    response = client.responses.create(
        model=MODEL_NAME,
        input=f"""
{SYSTEM_PROMPT}

ROADMAP:

{json.dumps(
    roadmap,
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

    try:

        result = json.loads(
            raw_response
        )

    except Exception:

        print(
            "\n===== INVALID JSON =====\n"
        )

        print(
            raw_response[:5000]
        )

        raise

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