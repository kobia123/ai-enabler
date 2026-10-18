# ssl_test.py

import requests

r = requests.get(
    "https://www.microsoft.com",
    verify=False
)

print(r.status_code)