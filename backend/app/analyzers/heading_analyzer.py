from bs4 import BeautifulSoup


def analyze_headings(data):

    soup = BeautifulSoup(data["html"], "html.parser")

    headings = {}

    total = 0

    heading_order = []

    for i in range(1, 7):
        tags = soup.find_all(f"h{i}")
        headings[f"h{i}"] = len(tags)

        for tag in tags:
            heading_order.append(i)

        total += len(tags)

    issues = []

    # ----------------------------
    # Missing H1
    # ----------------------------
    if headings["h1"] == 0:
        issues.append("Missing H1 tag")

    # ----------------------------
    # Multiple H1
    # ----------------------------
    if headings["h1"] > 1:
        issues.append("Multiple H1 tags found")

    # ----------------------------
    # Heading hierarchy validation
    # Example:
    # H1 -> H3 (missing H2)
    # H2 -> H4 (missing H3)
    # ----------------------------
    for i in range(1, len(heading_order)):
        previous = heading_order[i - 1]
        current = heading_order[i]

        if current - previous > 1:
            issues.append(
                f"Heading hierarchy skipped from H{previous} to H{current}"
            )

    if len(issues) == 0:
        status = "Good"
    else:
        status = "Needs Improvement"

    return {
        "h1": headings["h1"],
        "h2": headings["h2"],
        "h3": headings["h3"],
        "h4": headings["h4"],
        "h5": headings["h5"],
        "h6": headings["h6"],
        "total": total,
        "status": status,
        "issues": issues
    }