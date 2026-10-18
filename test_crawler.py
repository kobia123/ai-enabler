from crawler import get_page_text

url = "https://thejoint.org.il/about_us/"

content = get_page_text(url)

print(content[:3000])