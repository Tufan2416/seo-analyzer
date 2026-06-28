# API Documentation

## SEO Analyzer REST API

The SEO Analyzer backend is built using **FastAPI** and exposes RESTful endpoints for analyzing websites and retrieving SEO reports.

---

# Base URL

**Production**

```
https://seo-analyzer-production-5591.up.railway.app
```

**Local Development**

```
http://localhost:8000
```

---

# Authentication

Currently, the API does **not require authentication**.

Future versions may include JWT-based authentication for user accounts and report history.

---

# Endpoints

## 1. Analyze Website

Starts a new SEO analysis.

### Endpoint

```
POST /api/analyze
```

### Request Body

```json
{
  "url": "https://github.com"
}
```

### Request Parameters

| Parameter | Type   | Required | Description                   |
| --------- | ------ | -------- | ----------------------------- |
| url       | String | Yes      | Public website URL to analyze |

---

### Success Response

```json
{
  "job_id": "6b55f6f3-1234-5678-9012-acde12345678",
  "status": "completed"
}
```

---

### Error Response

```json
{
  "detail": "Invalid URL"
}
```

Status Code

```
400 Bad Request
```

---

## 2. Get Analysis Report

Retrieves the SEO report for a previously analyzed website.

### Endpoint

```
GET /api/results/{job_id}
```

### Path Parameter

| Parameter | Type        | Description             |
| --------- | ----------- | ----------------------- |
| job_id    | UUID/String | Analysis Job Identifier |

---

### Success Response

```json
{
  "job_id": "6b55f6f3-1234-5678-9012-acde12345678",
  "status": "completed",
  "result": {

    "url":"https://github.com",

    "meta": { },

    "headings": { },

    "images": { },

    "content": { },

    "technical": { },

    "performance": { },

    "security": { },

    "social": { },

    "structured_data": { },

    "score": { }

  }
}
```

---

### Error Response

```json
{
  "detail":"Job not found"
}
```

Status Code

```
404 Not Found
```

---

# API Workflow

```
Client
   │
   ▼
POST /api/analyze
   │
   ▼
FastAPI Backend
   │
   ▼
Crawler
   │
   ▼
SEO Analysis
   │
   ▼
Generate Report
   │
   ▼
Store Result
   │
   ▼
Return Job ID
   │
   ▼
GET /api/results/{job_id}
   │
   ▼
Return SEO Report
```

---

# Analyzer Modules

The API performs analysis using the following modules:

* Meta Analyzer
* Heading Analyzer
* Content Analyzer
* Image Analyzer
* URL Analyzer
* Link Analyzer
* Technical SEO Analyzer
* Performance Analyzer
* Social SEO Analyzer
* Security Analyzer
* Structured Data Analyzer
* Indexability Analyzer
* Core Web Vitals Analyzer
* SEO Score Calculator

---

# HTTP Status Codes

| Status Code | Description           |
| ----------- | --------------------- |
| 200         | Request Successful    |
| 400         | Invalid Request       |
| 404         | Resource Not Found    |
| 422         | Validation Error      |
| 500         | Internal Server Error |

---

# Swagger Documentation

Interactive API documentation is available at:

```
https://seo-analyzer-production-5591.up.railway.app/docs
```

OpenAPI specification:

```
https://seo-analyzer-production-5591.up.railway.app/openapi.json
```

---

# Example API Usage

### Analyze Website

```bash
curl -X POST \
https://seo-analyzer-production-5591.up.railway.app/api/analyze \
-H "Content-Type: application/json" \
-d '{
"url":"https://github.com"
}'
```

---

### Retrieve Report

```bash
curl \
https://seo-analyzer-production-5591.up.railway.app/api/results/{job_id}
```

---

# Future API Enhancements

* JWT Authentication
* Background Processing
* Bulk Website Analysis
* PDF Report Download
* Scheduled Website Monitoring
* Competitor Comparison API
* Rate Limiting
* API Keys
* Versioned API (v1, v2)

---

# Version

**Current Version:** v1.0

---

# Developed By

**Tufan Chowdhury**

GitHub:
https://github.com/Tufan2416

LinkedIn:
https://www.linkedin.com/in/tufan-chowdhury06/
