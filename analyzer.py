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
You are a senior enterprise architect and AI strategy consultant.

Analyze the organization.

Return VALID JSON ONLY.

Schema:

{
  "organization": {
    "name": "",
    "type": "",
    "mission": ""
  },

  "domains": [],

  "services": [],

  "programs": [],

  "target_populations": [],

  "partners": [],

  "strategic_goals": [],

  "business_functions": [
    {
      "name": "",
      "description": "",
      "roles": [],
      "activities": [],
      "documents": []
    }
  ],

  "process_candidates": [
    {
      "name": "",
      "description": "",
      "inputs": [],
      "outputs": [],
      "participants": []
    }
  ],

  "ai_opportunity_hints": [],

  "source_urls": []
}

Rules:

1. Return JSON only.
2. Do not invent facts.
3. Use empty arrays when information is unavailable.
4. Use empty strings when information is unavailable.
5. Extract information from the content.
6. Infer business functions only if strongly supported by the content.
7. For each business function identify:
   - description
   - roles
   - activities
   - documents
8. For each process identify:
   - inputs
   - outputs
   - participants
"""

def analyze_organization(text):
    print("Calling OpenAI...")

    response = client.responses.create(
        model="gpt-6-luna",
        input=f"""
{PROMPT}

CONTENT:

{text[:5000]}
"""
    )
    print("OpenAI completed")
    return json.loads(response.output_text)