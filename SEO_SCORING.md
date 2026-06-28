# SEO Scoring Methodology

## Overview

The SEO Analyzer calculates an overall SEO score between **0 and 100** by evaluating multiple aspects of a website's optimization. The scoring system is custom-built and designed to identify common SEO issues while providing actionable insights.

---

## Scoring Categories

| Category          | Purpose                                                        |
| ----------------- | -------------------------------------------------------------- |
| Meta Tags         | Evaluates title and meta description quality                   |
| Heading Structure | Checks H1-H6 hierarchy and heading organization                |
| Images            | Detects missing ALT attributes                                 |
| Technical SEO     | HTTPS, Robots.txt, Sitemap, Canonical URL, Mobile Friendliness |
| Content Analysis  | Content length, keyword usage, readability                     |
| Link Analysis     | Internal and external link evaluation                          |
| Performance       | Response time and page size                                    |
| Social SEO        | Open Graph and Twitter Card validation                         |
| Structured Data   | JSON-LD and Schema.org detection                               |
| Security          | HTTPS and SSL-related checks                                   |

---

## Score Calculation

The analyzer starts with a score of **100**.

Points are deducted when SEO issues are identified, such as:

* Missing title tag
* Poor title length
* Missing meta description
* Missing H1 tag
* Multiple H1 tags
* Incorrect heading hierarchy
* Missing image ALT attributes
* Missing robots.txt
* Missing sitemap.xml
* Missing canonical tag
* Slow page response
* Large page size
* Missing Open Graph tags
* Missing Twitter Cards

The remaining score is normalized to generate the final SEO score presented in the dashboard.

---

## Current Implementation

The scoring engine is implemented in:

```
backend/app/scoring/score.py
```

The score is generated after all analyzer modules complete their evaluation and is included in the final JSON response returned by the API.

---

## Future Improvements

* Weighted scoring based on SEO impact
* Google Lighthouse integration
* Core Web Vitals scoring
* AI-powered recommendation weighting
* Industry-specific scoring models
