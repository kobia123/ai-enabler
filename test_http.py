import requests
import certifi

try:
    r = requests.get(
        "https://api.openai.com/v1/models",
        timeout=30,
        verify=certifi.where()
    )

    print("STATUS:", r.status_code)
    print(r.text[:500])

except Exception as e:
    print(type(e))
    print(e)