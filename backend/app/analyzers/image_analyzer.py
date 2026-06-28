def analyze_images(data):
    images = data.get("images", [])

    total_images = len(images)
    missing_alt = 0

    for image in images:
        if not image.get("alt"):
            missing_alt += 1

    report = {
        "total_images": total_images,
        "missing_alt": missing_alt,
        "status": ""
    }

    if total_images == 0:
        report["status"] = "No Images Found"
    elif missing_alt == 0:
        report["status"] = "Good"
    else:
        report["status"] = "Missing ALT Tags"

    return report