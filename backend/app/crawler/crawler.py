from app.crawler.fetcher import fetch_page
from app.crawler.parser import parse_html
from app.crawler.extractor import extract_basic_data


def crawl(url: str):
    page = fetch_page(url)

    soup = parse_html(page["html"])

    data = extract_basic_data(soup, page["url"])

    return {
        "url": page["url"],
        "status": page["status_code"],
        "data": data,
    }