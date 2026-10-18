import json

import httpx
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL_NAME = "gpt-6.1-sol"

client = OpenAI(
    http_client=httpx.Client(
        verify=False,
        timeout=120
    )
)

SYSTEM_PROMPT = """
You are a senior AI strategist,
enterprise architect and transformation consultant.

You are given a business analysis.

Your objective is to identify and prioritize AI opportunities.

For each opportunity identify:

- use_case
- business_users
- required_data
- implementation_prerequisites
- risks
- safeguards

Assign:

- business_value
- impact_score
- complexity_score
- data_readiness_score
- priority

Impact Score:

1 = minimal value
2 = limited value
3 = moderate value
4 = significant value
5 = transformative value

Complexity Score:

1 = very easy
2 = easy
3 = moderate
4 = difficult
5 = highly complex

Data Readiness Score:

1 = unavailable
2 = limited
3 = moderate
4 = available
5 = highly available

Priority Rules:

P1:
impact_score >= 4
AND complexity_score <= 3
AND data_readiness_score >= 3

P2:
impact_score >= 3

P3:
all remaining opportunities

Guidelines:

- Generate practical AI opportunities.
- Focus on business value.
- Avoid duplicate opportunities.
- Use concise descriptions.
- Prefer enterprise-grade solutions.
- Include realistic risks and safeguards.

Return VALID JSON ONLY.

Schema:

{
  "ai_opportunities": [
    {
      "name": "",
      "use_case": "",
      "pattern_category": "",
      "copilot_pattern": "",
      "business_value": "",
      "impact_score": 0,
      "complexity_score": 0,
      "data_readiness_score": 0,
      "priority": "",
      "expected_value": "",
      "business_users": [],
      "required_data": [],
      "implementation_prerequisites": [],
      "risks": [],
      "safeguards": []
    }
  ]
}

Do not return markdown.
Do not wrap JSON in code fences.
Do not return explanations.
"""


def discover_opportunities(analysis):

    response = client.responses.create(
        model=MODEL_NAME,
        input=f"""
{SYSTEM_PROMPT}

BUSINESS ANALYSIS:

{json.dumps(
    analysis,
    ensure_ascii=False,
    indent=2
)}
"""
    )

    raw_response = response.output_text.strip()

    if not raw_response:
        raise Exception(
            "Empty response returned from model"
        )

    if raw_response.startswith("```"):
        raw_response = (
            raw_response
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