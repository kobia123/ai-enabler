import json

from openai import OpenAI
from dotenv import load_dotenv
import httpx

load_dotenv()

client = OpenAI(
    http_client=httpx.Client(
        verify=False,
        timeout=60
    )
)

PROMPT = """
You are a senior enterprise architect.

Expand each business function.

For every business function identify:

1. Purpose
2. Organizational roles
3. Daily activities
4. Documents
5. Systems
6. Pain points
7. AI opportunities

Return JSON only.

Schema:

{
  "expanded_functions": [
    {
      "name": "",
      "purpose": "",
      "roles": [],
      "activities": [],
      "documents": [],
      "systems": [],
      "pain_points": [],
      "ai_opportunities": []
    }
  ]
}
"""


def expand_functions(profile):

    business_functions = profile["business_functions"]

    response = client.responses.create(
        model="gpt-6.1-sol",
        input=f"""
{PROMPT}

BUSINESS FUNCTIONS:

{json.dumps(business_functions, ensure_ascii=False)}
"""
    )

    return json.loads(response.output_text)