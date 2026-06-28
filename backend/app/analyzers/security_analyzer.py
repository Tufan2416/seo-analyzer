import requests


def analyze_security(url):

    report = {}

    try:

        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        headers = response.headers

        checks = {
            "Strict-Transport-Security": "hsts",
            "Content-Security-Policy": "csp",
            "X-Frame-Options": "x_frame",
            "X-Content-Type-Options": "content_type",
            "Referrer-Policy": "referrer",
            "Permissions-Policy": "permissions"
        }

        found = 0

        for header, key in checks.items():

            exists = header in headers

            report[key] = exists

            if exists:
                found += 1

        report["headers_found"] = found
        report["headers_missing"] = len(checks) - found
        report["score"] = int((found / len(checks)) * 100)

    except Exception as e:

        report = {
            "headers_found": 0,
            "headers_missing": 6,
            "score": 0,
            "error": str(e)
        }

    return report