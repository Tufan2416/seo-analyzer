import requests
import time


def analyze_core_web_vitals(url):

    start = time.time()

    try:
        response = requests.get(url, timeout=10)
        load_time = round(time.time() - start, 2)

        page_size = round(len(response.content) / 1024, 2)

        return {

            "load_time": load_time,

            "page_size_kb": page_size,

            "status_code": response.status_code,

            "compression": response.headers.get(
                "Content-Encoding",
                "None"
            ),

            "cache_control": response.headers.get(
                "Cache-Control",
                "Missing"
            ),

            "server": response.headers.get(
                "Server",
                "Unknown"
            )

        }

    except Exception as e:

        return {

            "error": str(e)

        }