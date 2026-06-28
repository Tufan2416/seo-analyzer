import time
import requests


def analyze_performance(url):
    start = time.time()

    response = requests.get(url, timeout=15)

    end = time.time()

    response_time = round(end - start, 2)

    page_size = round(len(response.content) / 1024, 2)

    return {
        "response_time_seconds": response_time,
        "page_size_kb": page_size,
        "status_code": response.status_code
    }