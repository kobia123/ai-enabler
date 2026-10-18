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
You are a senior enterprise architect and business analyst.

Analyze ONE business function.

Your objective is to understand and document the business function.

Identify:

1. Function purpose

2. Business pain points

3. Supporting systems

4. Business KPIs

5. Overall confidence level

Use only the provided information whenever possible.

When information is missing:

- make reasonable enterprise assumptions
- explicitly mark assumptions using confidence levels
- do not present assumptions as facts

Confidence Levels:

high
= explicitly supported by supplied content

medium
= strongly inferred from supplied content

low
= assumption requiring validation

Guidelines:

- Focus on business understanding only.
- Focus on current-state analysis.
- Be concise and factual.
- Avoid excessive explanations.
- Do not generate AI recommendations.
- Do not suggest AI use cases.
- Do not recommend Copilots.
- Do not prioritize opportunities.
- Do not score impact, complexity or readiness.
- Do not include implementation guidance.

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

  "systems": [
    {
      "name": "",
      "purpose": ""
    }
  ],

  "kpis": [
    {
      "name": "",
      "definition": ""
    }
  ]
}

Return JSON only.

Do not return markdown.

Do not wrap JSON in code fences.

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