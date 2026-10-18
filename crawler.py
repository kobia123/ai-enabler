import requests
from bs4 import BeautifulSoup


def get_page_text(url):
    response = requests.get(
        url,
        verify=False,
        timeout=30
    )

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(separator=" ", strip=True)

    return text