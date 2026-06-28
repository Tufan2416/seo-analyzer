def analyze_headings(data):

    headings = data["headings"]

    counts = {}

    total = 0

    issues = []

    previous = 0

    for i in range(1, 7):

        tag = f"h{i}"

        counts[tag] = len(headings.get(tag, []))

        total += counts[tag]

        if counts[tag] > 0:

            if previous != 0 and i - previous > 1:
                issues.append(
                    f"Heading hierarchy skipped from H{previous} to H{i}"
                )

            previous = i

    if counts["h1"] == 0:
        issues.append("Missing H1 tag")

    elif counts["h1"] > 1:
        issues.append("Multiple H1 tags found")

    status = "Good" if len(issues) == 0 else "Needs Improvement"

    return {
        "h1": counts["h1"],
        "h2": counts["h2"],
        "h3": counts["h3"],
        "h4": counts["h4"],
        "h5": counts["h5"],
        "h6": counts["h6"],
        "total": total,
        "status": status,
        "issues": issues
    }