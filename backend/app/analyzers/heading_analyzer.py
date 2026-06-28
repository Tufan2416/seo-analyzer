def analyze_headings(data):
    headings = data.get("headings", {})

    h1 = headings.get("h1", [])
    h2 = headings.get("h2", [])

    report = {
        "h1_count": len(h1),
        "h2_count": len(h2),
        "total_headings": sum(len(v) for v in headings.values()),
        "status": ""
    }

    if len(h1) == 0:
        report["status"] = "Missing H1"
    elif len(h1) > 1:
        report["status"] = "Multiple H1"
    else:
        report["status"] = "Good"

    return report