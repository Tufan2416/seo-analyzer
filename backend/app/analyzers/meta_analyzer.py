def analyze_meta(data):
    title = data.get("title", "")
    description = data.get("meta_description", "")

    report = {
        "title": {
            "exists": bool(title),
            "length": len(title),
            "status": ""
        },
        "meta_description": {
            "exists": bool(description),
            "length": len(description),
            "status": ""
        }
    }

    # Title Analysis
    if not title:
        report["title"]["status"] = "Missing"
    elif 50 <= len(title) <= 60:
        report["title"]["status"] = "Good"
    else:
        report["title"]["status"] = "Needs Improvement"

    # Meta Description Analysis
    if not description:
        report["meta_description"]["status"] = "Missing"
    elif 120 <= len(description) <= 160:
        report["meta_description"]["status"] = "Good"
    else:
        report["meta_description"]["status"] = "Needs Improvement"

    return report