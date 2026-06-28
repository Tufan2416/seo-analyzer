def calculate_score(report):

    technical_score = 100

    # Meta
    if report["meta"]["title"]["status"] != "Good":
        technical_score -= 10

    if report["meta"]["meta_description"]["status"] != "Good":
        technical_score -= 10

    # Headings
    if report["headings"]["status"] != "Good":
        technical_score -= 10

    # Images
    if report["images"]["missing_alt"] > 0:
        technical_score -= 10

    # Technical
    if not report["technical"]["https"]:
        technical_score -= 10

    if not report["technical"]["robots_txt"]:
        technical_score -= 5

    if not report["technical"]["sitemap_xml"]:
        technical_score -= 5

    if not report["technical"]["mobile_friendly"]:
        technical_score -= 5

    if not report["technical"]["canonical"]:
        technical_score -= 5

    # Indexability
    if not report["indexability"]["indexable"]:
        technical_score -= 10

    # Structured Data
    if report["structured_data"]["total"] == 0:
        technical_score -= 10

    # Security
    technical_score = int(
        (technical_score + report["security"]["score"]) / 2
    )

    technical_score = max(technical_score, 0)

    # Performance
    performance_score = 100

    if report["performance"]["response_time_seconds"] > 2:
        performance_score -= 20

    if report["performance"]["page_size_kb"] > 2000:
        performance_score -= 20

    if report.get("core_web_vitals"):

        if report["core_web_vitals"].get("load_time", 0) > 3:
            performance_score -= 20

    performance_score = max(performance_score, 0)

    # Content
    content_score = 100

    if report["content"]["word_count"] < 300:
        content_score -= 20

    if report["content"]["readability"] != "Good":
        content_score -= 20

    content_score = max(content_score, 0)

    # Social
    social_score = 100

    if len(report["social"]["open_graph"]) == 0:
        social_score -= 50

    if len(report["social"]["twitter"]) == 0:
        social_score -= 50

    social_score = max(social_score, 0)

    # Overall
    overall_score = int(
        (
            technical_score
            + performance_score
            + content_score
            + social_score
        ) / 4
    )

    return {
        "technical_score": technical_score,
        "performance_score": performance_score,
        "content_score": content_score,
        "social_score": social_score,
        "overall_score": overall_score
    }