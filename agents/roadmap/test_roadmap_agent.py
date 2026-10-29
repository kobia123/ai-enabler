from agents.roadmap.agent import RoadmapAgent


agent = RoadmapAgent()


test_insights = {
    "function_insights": [
        {
            "name": "Human Resources",
            "ai_opportunities": [
                {
                    "name": "Resume Screening",
                    "impact_score": 8,
                    "complexity_score": 3
                }
            ]
        },
        {
            "name": "Finance",
            "ai_opportunities": [
                {
                    "name": "Invoice Processing",
                    "impact_score": 9,
                    "complexity_score": 4
                }
            ]
        }
    ]
}


result = agent.execute(
    {
        "insights": test_insights
    }
)

print("\n=== EXECUTION RESULT ===")
print(result)