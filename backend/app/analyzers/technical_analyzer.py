import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def analyze_technical(url):
    report = {}

    report["https"] = url.startswith("https://")

    try:
        robots = requests.get(urljoin(url, "/robots.txt"), timeout=10)
        report["robots_txt"] = robots.status_code == 200
    except Exception:
        report["robots_txt"] = False

    try:
        sitemap = requests.get(urljoin(url, "/sitemap.xml"), timeout=10)
        report["sitemap_xml"] = sitemap.status_code == 200
    except Exception:
        report["sitemap_xml"] = False

    # Fetch page safely
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        canonical = soup.find("link", rel="canonical")
        report["canonical"] = (
            canonical["href"]
            if canonical and canonical.get("href")
            else None
        )

        viewport = soup.find("meta", attrs={"name": "viewport"})
        report["mobile_friendly"] = viewport is not None

        structured = soup.find_all(
            "script",
            attrs={"type": "application/ld+json"}
        )
        report["structured_data"] = len(structured)

        report["redirected"] = response.url != url

    except requests.RequestException as e:
        report["canonical"] = None
        report["mobile_friendly"] = False
        report["structured_data"] = 0
        report["redirected"] = False
        report["error"] = str(e)

    return report