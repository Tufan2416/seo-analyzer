import requests
from bs4 import BeautifulSoup


def analyze_indexability(url):

    report = {}

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(response.text, "lxml")

        # --------------------
        # Meta Robots
        # --------------------
        robots = soup.find("meta", attrs={"name": "robots"})

        if robots:

            content = robots.get("content", "").lower()

            report["meta_robots"] = content
            report["noindex"] = "noindex" in content
            report["nofollow"] = "nofollow" in content

        else:

            report["meta_robots"] = None
            report["noindex"] = False
            report["nofollow"] = False

        # --------------------
        # X-Robots Header
        # --------------------
        xrobots = response.headers.get("X-Robots-Tag")

        report["x_robots_tag"] = xrobots if xrobots else None

        # --------------------
        # Indexable
        # --------------------
        report["indexable"] = (
            not report["noindex"]
        )

    except Exception as e:

        report = {
            "meta_robots": None,
            "noindex": False,
            "nofollow": False,
            "x_robots_tag": None,
            "indexable": False,
            "error": str(e)
        }

    return report