# Backend Architecture

## Overview

The backend is built using **FastAPI** and follows a modular architecture where each SEO analyzer operates independently. This design improves maintainability, scalability, and allows new analyzers to be added with minimal changes.

---

## Architecture Flow

```
                 User
                   │
                   ▼
          React Frontend
              (Vercel)
                   │
          HTTP REST Request
                   │
                   ▼
         FastAPI Backend
             (Railway)
                   │
             SEO Service
                   │
         Website Crawler
                   │
      HTML Parsing (BeautifulSoup)
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
 Meta Analyzer  Heading Analyzer  Image Analyzer
      ▼            ▼            ▼
 Link Analyzer  Content Analyzer  Technical Analyzer
      ▼
 Performance Analyzer
      ▼
 Security Analyzer
      ▼
 Social Analyzer
      ▼
 Structured Data Analyzer
      ▼
 Indexability Analyzer
      ▼
 SEO Score Calculator
      ▼
 JSON Response
```

---

## Request Workflow

1. User submits a website URL.
2. React frontend sends a POST request to `/api/analyze`.
3. FastAPI receives the request.
4. The crawler downloads the webpage.
5. BeautifulSoup parses the HTML.
6. Individual analyzers evaluate specific SEO categories.
7. Results are combined into a single report.
8. The scoring engine calculates the overall SEO score.
9. The backend returns a JSON response.
10. React renders the report in the dashboard.

---

## Project Structure

```
backend/
│
├── api/
├── analyzers/
├── crawler/
├── database/
├── models/
├── scoring/
├── services/
└── main.py
```

---

## Design Principles

* Modular architecture
* Separation of concerns
* RESTful API design
* Independent analyzer modules
* Scalable service layer
* Easy future expansion
