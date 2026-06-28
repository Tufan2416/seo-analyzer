import re


def analyze_content(data):
    content = data.get("content", "")
    headings = data.get("headings", {})

    words = re.findall(r"\w+", content)

    word_count = len(words)

    keyword = ""

    if words:
        keyword = words[0].lower()

    keyword_count = sum(
        1 for word in words
        if word.lower() == keyword
    )

    total_headings = sum(
        len(v) for v in headings.values()
    )

    report = {
        "word_count": word_count,
        "keyword_checked": keyword,
        "keyword_occurrences": keyword_count,
        "heading_count": total_headings,
        "readability": ""
    }

    if word_count < 300:
        report["readability"] = "Content Too Short"
    elif word_count < 800:
        report["readability"] = "Average"
    else:
        report["readability"] = "Good"

    return report