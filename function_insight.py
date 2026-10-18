import json

from openai import OpenAI
from dotenv import load_dotenv
import httpx

load_dotenv()

PROMPT_VERSION = "1.0"

MODEL_NAME = "gpt-6.1-sol"

client = OpenAI(
    http_client=httpx.Client(
        verify=False,
        timeout=120
    )
)

SYSTEM_PROMPT = """
You are a senior enterprise architect, business analyst,
AI strategist and transformation consultant.

Analyze ONE business function.

Your objective is to identify:

1. Function purpose
2. Business pain points
3. Supporting systems
4. Information flows
5. Business KPIs
6. AI opportunities
7. Implementation readiness
8. Recommended AI patterns
9. Opportunity prioritization

Use only provided information whenever possible.

When information is missing:

- make reasonable enterprise assumptions
- explicitly mark assumptions using confidence levels
- do not present assumptions as facts

Confidence Levels:

high = explicitly supported by supplied content

medium = strongly inferred from supplied content

low = assumption requiring validation

Business Value:

low
medium
high
very_high

Impact Score:

1 = minimal value
2 = limited value
3 = moderate value
4 = significant value
5 = transformative value

Complexity Score:

1 = very easy implementation
2 = easy implementation
3 = moderate implementation
4 = difficult implementation
5 = highly complex implementation

Data Readiness Score:

1 = required data mostly unavailable
2 = data partially available
3 = moderate availability
4 = good availability
5 = strong availability and quality

Priority Rules:

P1:
impact_score >= 4
AND complexity_score <= 3
AND data_readiness_score >= 3

P2:
impact_score >= 3

P3:
all others

Return VALID JSON ONLY.

Schema:

{
  "name": "",
  "purpose": "",
  "overall_confidence": "",

  "pain_points": [
    {
      "name": "",
      "description": "",
      "confidence": "",
      "business_impact": ""
    }
  ],

  "systems": [],

  "information_flows": [],

  "kpis": [],

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

Return JSON only.
Do not wrap JSON in markdown.
Do not return explanations.
"""


def analyze_function(function):

    user_prompt = f"""
Analyze the following business function.

BUSINESS FUNCTION:

{json.dumps(function, ensure_ascii=False, indent=2)}
"""

    response = client.responses.create(
        model=MODEL_NAME,
        input=f"""
{SYSTEM_PROMPT}

{user_prompt}
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

        print("\n===== INVALID JSON =====\n")

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