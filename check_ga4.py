import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

visited = set()
pages_without_ga4 = []

def has_ga4(html):
    return (
        re.search(r"gtag\(['\"]config['\"],\s*['\"]G-[A-Z0-9]+['\"]\)", html) or
        re.search(r"https://www\.googletagmanager\.com/gtag/js\?id=G-[A-Z0-9]+", html)
    )

def crawl(url, base_url, max_pages=100):
    if url in visited or len(visited) >= max_pages:
        return

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return
        visited.add(url)

        html = response.text
        if not has_ga4(html):
            pages_without_ga4.append(url)
            print(f"[❌] GA4 NOT found: {url}")
        else:
            print(f"[✅] GA4 found: {url}")

        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", href=True):
            href = link["href"]
            joined_url = urljoin(base_url, href)
            if urlparse(joined_url).netloc == urlparse(base_url).netloc:
                crawl(joined_url.split("#")[0], base_url, max_pages)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

if __name__ == "__main__":
    start_url = input("Enter the base URL (e.g., https://example.com): ").strip()
    max_pages = int(input("Max pages to scan (e.g., 50): ").strip())
    crawl(start_url, start_url, max_pages)

    print("\n=== Pages Without GA4 ===")
    for page in pages_without_ga4:
        print(page)

