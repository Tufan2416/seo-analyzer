import requests
from bs4 import BeautifulSoup


def analyze_structured_data(url):

    report = {}

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(response.text, "lxml")

        json_ld = soup.find_all(
            "script",
            attrs={"type": "application/ld+json"}
        )

        microdata = soup.find_all(attrs={"itemscope": True})

        rdfa = soup.find_all(attrs={"property": True})

        report["json_ld"] = len(json_ld)
        report["microdata"] = len(microdata)
        report["rdfa"] = len(rdfa)

        total = (
            len(json_ld)
            + len(microdata)
            + len(rdfa)
        )

        report["total"] = total

        if total == 0:
            report["status"] = "Missing"
        elif total < 3:
            report["status"] = "Needs Improvement"
        else:
            report["status"] = "Good"

    except Exception as e:

        report = {
            "json_ld": 0,
            "microdata": 0,
            "rdfa": 0,
            "total": 0,
            "status": "Error",
            "error": str(e)
        }

    return report