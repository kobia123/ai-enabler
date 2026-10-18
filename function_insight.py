import json

from openai import OpenAI
from dotenv import load_dotenv
import httpx

load_dotenv()

PROMPT_VERSION = "3.0"

MODEL_NAME = "gpt-6.1-sol"

client = OpenAI(
    http_client=httpx.Client(
        verify=False,
        timeout=300
    )
)

SYSTEM_PROMPT = """
You are a senior enterprise architect,
business analyst,
AI strategist,
and transformation consultant.

Analyze ONE business function.

Your objective is to identify:

1. Function purpose
2. Business pain points
3. Supporting systems
4. Information flows
5. Business KPIs
6. AI opportunities
7. Opportunity prioritization

Use only provided information whenever possible.

When information is missing:

- make reasonable assumptions
- mark assumptions using confidence levels
- do not present assumptions as facts

Confidence Levels:

high = directly supported
medium = strongly inferred
low = assumption requiring validation

Business Value:

low
medium
high
very_high

Impact Score:

1 = minimal
2 = limited
3 = moderate
4 = significant
5 = transformative

Complexity Score:

1 = very easy
2 = easy
3 = moderate
4 = difficult
5 = highly complex

Data Readiness Score:

1 = unavailable
2 = partial
3 = moderate
4 = good
5 = strong

Consider opportunities across:

- Knowledge Management
- Process Automation
- Decision Intelligence
- Predictive Analytics
- Agentic AI
- Employee Productivity
- Customer/Citizen Experience

Every opportunity MUST use one of these values
for "pattern_category".

Generate a diverse portfolio.

Do not generate more than two opportunities
from the same category.

Keep responses concise.

For pain points:
- short name only

For systems:
- system name only

For information flows:
- source and destination only

For KPIs:
- KPI name only

For AI opportunities:
- use_case = one sentence maximum
- no business_users
- no required_data
- no implementation_prerequisites
- no risks
- no safeguards
- no expected_value

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
      "confidence": ""
    }
  ],

  "systems": [
    {
      "name": "",
      "confidence": ""
    }
  ],

  "information_flows": [
    {
      "source": "",
      "destination": ""
    }
  ],

  "kpis": [
    {
      "name": "",
      "confidence": ""
    }
  ],

  "ai_opportunities": [
    {
      "name": "",
      "pattern_category": "",
      "use_case": "",
      "business_value": "",

      "impact_score": 0,
      "complexity_score": 0,
      "data_readiness_score": 0,

      "priority": ""
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

    raw_response = (
        response.output_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    if not raw_response:

        raise Exception(
            "Empty response returned from model"
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