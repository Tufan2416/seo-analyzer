def analyze_url(url: str):
    report = {
        "url": url,
        "length": len(url),
        "https": url.startswith("https://"),
        "status": ""
    }

    if not report["https"]:
        report["status"] = "Not Secure (HTTP)"
    elif report["length"] <= 75:
        report["status"] = "Good"
    else:
        report["status"] = "URL Too Long"

    return report