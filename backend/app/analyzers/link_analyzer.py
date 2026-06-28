from urllib.parse import urlparse


def analyze_links(data, base_url):
    links = data.get("links", [])

    domain = urlparse(base_url).netloc

    internal = 0
    external = 0

    for link in links:
        if urlparse(link).netloc == domain:
            internal += 1
        else:
            external += 1

    return {
        "total_links": len(links),
        "internal_links": internal,
        "external_links": external
    }