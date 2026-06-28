from app.crawler.crawler import crawl

from app.analyzers.content_analyzer import analyze_content
from app.analyzers.meta_analyzer import analyze_meta
from app.analyzers.heading_analyzer import analyze_headings
from app.analyzers.image_analyzer import analyze_images
from app.analyzers.url_analyzer import analyze_url
from app.analyzers.link_analyzer import analyze_links
from app.analyzers.technical_analyzer import analyze_technical
from app.analyzers.performance_analyzer import analyze_performance
from app.analyzers.social_analyzer import analyze_social
from app.analyzers.core_web_vitals import analyze_core_web_vitals
from app.analyzers.indexability_analyzer import analyze_indexability
from app.analyzers.security_analyzer import analyze_security
from app.analyzers.structured_data_analyzer import analyze_structured_data

from app.scoring.score import calculate_score


def generate_report(url: str):

    try:
        crawl_result = crawl(url)
        data = crawl_result["data"]

    except Exception as e:
        return {
            "url": url,
            "status": "failed",
            "error": str(e)
        }

    report = {
        "url": crawl_result["url"],

        "meta": analyze_meta(data),

        "headings": analyze_headings(data),

        "images": analyze_images(data),

        "url_analysis": analyze_url(crawl_result["url"]),

        "content": analyze_content(data),
        
        "social": analyze_social(url),
        
        "indexability": analyze_indexability(
            crawl_result["url"]
        ),

        "links": analyze_links(
            data,
            crawl_result["url"]
        ),

        "performance": analyze_performance(
            crawl_result["url"]
        ),
        
        "core_web_vitals": analyze_core_web_vitals(
            crawl_result["url"]
        ),
        
        "security": analyze_security(
            crawl_result["url"]
        ),
        
        "structured_data": analyze_structured_data(
            crawl_result["url"]
        ),

        "technical": analyze_technical(
            crawl_result["url"]
        )
    }

    # Calculate score AFTER report is created
    report["score"] = calculate_score(report)

    return report