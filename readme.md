# SEO Analyzer

A full-stack SEO Analyzer inspired by Woorank that performs comprehensive website SEO audits using custom-built logic, manual crawling, and open-source libraries.

> No Woorank APIs or paid SEO APIs are used.

---

## Live Demo

**Frontend:** https://seo-analyzer-olive.vercel.app

**Backend API (Swagger):**
https://seo-analyzer-production-5591.up.railway.app/docs

**GitHub Repository:**
https://github.com/Tufan2416/seo-analyzer

---

# Project Overview

The SEO Analyzer evaluates websites by crawling their pages and generating a detailed SEO report.

The project was developed to replicate the core functionality of Woorank using:

- Custom crawling
- Open-source libraries
- FastAPI backend
- React frontend

No paid SEO services or Woorank APIs are used.

---

# Features

## On-Page SEO Analysis

- Meta Title Analysis
- Meta Description Analysis
- Heading Structure (H1-H6)
- Multiple H1 Detection
- Image ALT Tag Analysis
- URL Structure Analysis
- Content Analysis
- Keyword Detection
- Content Length Analysis

---

## Technical SEO

- HTTPS Detection
- robots.txt Detection
- sitemap.xml Detection
- Mobile Friendly Detection
- Canonical Tag Detection
- Redirect Handling
- Indexability Analysis

---

## Link Analysis

- Internal Links Count
- External Links Count
- Total Links

---

## Performance Analysis

- Response Time
- Page Size
- HTTP Status Code

---

## Social SEO

- Open Graph Tags
- Twitter Cards
- Social Metadata Detection

---

## Security Analysis

- HTTPS Validation
- SSL Availability

---

## Structured Data

- JSON-LD Detection
- Schema.org Detection

---

## SEO Recommendations

The analyzer automatically generates recommendations such as:

- Improve Meta Title
- Improve Meta Description
- Add Missing ALT Tags
- Use Single H1
- Improve Mobile Friendliness
- Add Sitemap
- Improve Social Metadata

---

# SEO Score System

The application generates an overall SEO score out of 100.

The score is calculated from multiple categories:

| Category | Weight |
|----------|----------|
| Technical SEO | 25% |
| Performance | 25% |
| Content Quality | 25% |
| Social SEO | 25% |

Each category evaluates multiple SEO factors and contributes equally to the final score.

The scoring system is custom-built and does not rely on external SEO scoring services.

---

# Backend Architecture

```
Frontend (React)

        │

        ▼

FastAPI REST API

        │

        ▼

Crawler

        │

        ▼

SEO Analyzer Modules

├── Meta Analyzer
├── Heading Analyzer
├── Image Analyzer
├── URL Analyzer
├── Link Analyzer
├── Technical Analyzer
├── Content Analyzer
├── Performance Analyzer
├── Social Analyzer
├── Indexability Analyzer
├── Security Analyzer
├── Structured Data Analyzer
└── Core Web Vitals Analyzer

        │

        ▼

SEO Score Engine

        │

        ▼

JSON Report
```

---

# API Endpoints

## POST

```
POST /api/analyze
```

Starts a new SEO analysis.

Example

```json
{
    "url":"https://github.com"
}
```

Returns

```json
{
    "job_id":"xxxx",
    "status":"processing"
}
```

---

## GET

```
GET /api/results/{job_id}
```

Returns the SEO report.

---

# Technology Stack

## Frontend

- React
- Vite
- Axios

## Backend

- FastAPI
- BeautifulSoup4
- Requests
- Uvicorn

## Deployment

Frontend

- Vercel

Backend

- Railway

---

# Project Structure

```
seo-analyzer/

├── backend/
│   ├── app/
│   │   ├── analyzers/
│   │   ├── crawler/
│   │   ├── api/
│   │   ├── services/
│   │   ├── scoring/
│   │   └── utils/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── docker-compose.yml
```

---

# Installation

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# Deployment

## Backend

Railway

## Frontend

Vercel

---

# Project Requirements Coverage

| Requirement | Status |
|-------------|--------|
| Meta Analysis | ✅ |
| Heading Analysis | ✅ |
| Image ALT Analysis | ✅ |
| URL Analysis | ✅ |
| Internal Links | ✅ |
| External Links | ✅ |
| HTTPS Check | ✅ |
| robots.txt | ✅ |
| sitemap.xml | ✅ |
| Mobile Friendly | ✅ |
| Canonical Tag | ✅ |
| Redirect Handling | ✅ |
| Indexability | ✅ |
| Structured Data | ✅ |
| Performance Metrics | ✅ |
| Content Analysis | ✅ |
| Keyword Detection | ✅ |
| Readability | ✅ |
| Open Graph | ✅ |
| Twitter Cards | ✅ |
| SEO Score | ✅ |
| FastAPI API | ✅ |
| React Frontend | ✅ |
| Railway Deployment | ✅ |
| Vercel Deployment | ✅ |

---

# Future Improvements

- Google Lighthouse Integration
- Real Core Web Vitals API
- PDF Report Export
- Scheduled SEO Monitoring
- Historical SEO Reports
- Multi-page Crawling
- Competitor SEO Comparison

---

# Author

**Tufan Chowdhury**

B.Tech Computer Science Engineering

GitHub:
https://github.com/Tufan2416

LinkedIn:
https://www.linkedin.com/in/tufan-chowdhury06/

---

# License

This project was developed for educational and project submission purposes.
