import requests
from bs4 import BeautifulSoup


def analyze_social(url):
    report = {}

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "lxml")

        report["open_graph"] = {
            "title": soup.find("meta", property="og:title") is not None,
            "description": soup.find("meta", property="og:description") is not None,
            "image": soup.find("meta", property="og:image") is not None,
            "url": soup.find("meta", property="og:url") is not None,
        }

        report["twitter"] = {
            "card": soup.find("meta", attrs={"name": "twitter:card"}) is not None,
            "title": soup.find("meta", attrs={"name": "twitter:title"}) is not None,
            "description": soup.find("meta", attrs={"name": "twitter:description"}) is not None,
            "image": soup.find("meta", attrs={"name": "twitter:image"}) is not None,
        }

        score = 0

        score += sum(report["open_graph"].values()) * 12.5
        score += sum(report["twitter"].values()) * 12.5

        report["score"] = int(score)

        return report

    except Exception as e:
        return {
            "error": str(e)
        }