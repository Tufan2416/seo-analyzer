from urllib.parse import urljoin

def extract_basic_data(soup, base_url):
    title = soup.title.string.strip() if soup.title and soup.title.string else ""

    meta_description = ""

    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        meta_description = meta.get("content", "")

    headings = {}

    for i in range(1, 7):
        tag = f"h{i}"
        headings[tag] = [h.get_text(strip=True) for h in soup.find_all(tag)]

    # ---------------- Images ----------------

    images = []

    for img in soup.find_all("img"):
        images.append({
            "src": urljoin(base_url, img.get("src", "")),
            "alt": img.get("alt", "")
        })

    # ---------------- Links ----------------

    links = []

    for link in soup.find_all("a", href=True):
        links.append(urljoin(base_url, link["href"]))
    content = soup.get_text(separator=" ", strip=True)     

    return {
        "title": title,
        "meta_description": meta_description,
        "headings": headings,
        "images": images,
        "links": links,
        "content": content
    }