# 🚀 SEO Analyzer

<div align="center">

![React](https://img.shields.io/badge/React-19-blue?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.12-yellow?logo=python)
![Vercel](https://img.shields.io/badge/Frontend-Vercel-green?logo=vercel)
![Railway](https://img.shields.io/badge/Backend-Railway-purple?logo=railway)
![License](https://img.shields.io/badge/License-MIT-blue)

**A full-stack SEO analysis platform that evaluates website performance, technical SEO, metadata, content quality, security, and overall optimization using FastAPI and React.**

</div>

---

## 🌐 Live Demo

**Frontend:**  
https://seo-analyzer-olive.vercel.app/

**Backend API:**  
https://seo-analyzer-production-5591.up.railway.app

**Swagger API Documentation:**  
https://seo-analyzer-production-5591.up.railway.app/docs

---

# 📖 Project Overview

SEO Analyzer is a full-stack web application that performs comprehensive SEO analysis for any public website.

The application crawls a webpage, extracts important SEO information, evaluates multiple optimization factors, calculates an overall SEO score, and provides actionable recommendations to improve search engine visibility.

The frontend is developed using **React + Vite**, while the backend uses **FastAPI** with a modular analyzer architecture. The application is deployed using **Vercel** (Frontend) and **Railway** (Backend).

---

# ✨ Features

- 🔍 Analyze any public website
- 📊 Overall SEO Score (0–100)
- 📝 Meta Title & Description Analysis
- 🏷 Heading Structure Validation (H1–H6)
- 🖼 Image ALT Attribute Analysis
- 🔗 Internal & External Link Analysis
- 📄 Content Quality Analysis
- ⚡ Performance Metrics
- 🔒 HTTPS & Security Checks
- 🌐 Technical SEO Analysis
- 📱 Mobile Friendliness Detection
- 🤝 Social SEO Analysis (Open Graph & Twitter Cards)
- 📈 Structured Data Detection
- 📑 Robots.txt & Sitemap Validation
- 📚 Interactive Swagger API Documentation
- 📱 Responsive UI

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- Axios
- Tailwind CSS

## Backend

- FastAPI
- BeautifulSoup4
- Requests
- Uvicorn

## Deployment

- Vercel
- Railway
- GitHub

---

# 📂 Project Structure

```
seo-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── analyzers/
│   │   ├── api/
│   │   ├── crawler/
│   │   ├── scoring/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── assets/
│   │   ├── components/
│   │   └── App.jsx
│   │
│   └── package.json
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Tufan2416/seo-analyzer.git

cd seo-analyzer
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run backend

```bash
uvicorn main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

Backend runs at

```
http://localhost:8000
```

---
