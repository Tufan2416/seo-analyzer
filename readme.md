# 🚀 SEO Analyzer

An AI-powered SEO auditing platform that analyzes websites and generates comprehensive SEO reports with actionable recommendations. Built with **FastAPI**, **React (Vite)**, **Docker**, and deployed using **Railway** and **Vercel**.

## 🌐 Live Demo

**Frontend:** https://seo-analyzer-olive.vercel.app

**Backend API:** https://seo-analyzer-production-5591.up.railway.app

**API Documentation:** https://seo-analyzer-production-5591.up.railway.app/docs

---

## 📌 Features

### On-Page SEO
- ✅ Title Tag Analysis
- ✅ Meta Description Analysis
- ✅ Heading Structure (H1-H6)
- ✅ Content Quality Analysis
- ✅ Keyword Occurrence Analysis

### Technical SEO
- ✅ HTTPS Detection
- ✅ Robots.txt Detection
- ✅ Sitemap.xml Detection
- ✅ Canonical Tag Detection
- ✅ Mobile Friendly Check
- ✅ Redirect Detection

### Media Analysis
- ✅ Image Count
- ✅ Missing ALT Attributes

### Link Analysis
- ✅ Internal Links
- ✅ External Links
- ✅ Total Links

### Performance Analysis
- ✅ Response Time
- ✅ Page Size
- ✅ HTTP Status Code

### Social SEO
- ✅ Open Graph Tags
- ✅ Twitter Card Detection

### Advanced SEO
- ✅ Structured Data Detection
- ✅ Security Analysis
- ✅ Indexability Analysis
- ✅ Core Web Vitals (Basic Analysis)

### SEO Scoring
- ✅ Technical Score
- ✅ Performance Score
- ✅ Content Score
- ✅ Social Score
- ✅ Overall SEO Score

---

## 🛠 Tech Stack

### Frontend
- React.js
- Vite
- Tailwind CSS
- Axios

### Backend
- FastAPI
- BeautifulSoup4
- Requests
- lxml
- Uvicorn

### Deployment
- Railway (Backend)
- Vercel (Frontend)
- Docker
- GitHub

---

## 📂 Project Structure

```
seo-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── analyzers/
│   │   ├── crawler/
│   │   ├── api/
│   │   ├── scoring/
│   │   └── services/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   └── assets/
│   └── package.json
│
└── docker-compose.yml
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Tufan2416/seo-analyzer.git
cd seo-analyzer
```

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 🐳 Docker

```bash
docker compose up --build
```

---

## 📈 Sample Report Includes

- Overall SEO Score
- Meta Analysis
- Heading Analysis
- Image SEO
- Technical SEO
- Performance Metrics
- Social SEO
- Link Analysis
- Content Analysis
- Security Analysis
- Indexability
- Structured Data
- Recommendations

---

## 🎯 Future Improvements

- Google PageSpeed Insights API Integration
- Lighthouse Integration
- PDF Report Generation
- Website Audit History
- User Authentication
- Scheduled SEO Monitoring
- Competitor Analysis
- AI-Powered SEO Recommendations

---

## 👨‍💻 Author

**Tufan Chowdhury**

GitHub: https://github.com/Tufan2416

LinkedIn: https://www.linkedin.com/in/tufan-chowdhury06/

---

## 📄 License

This project is developed for educational purposes and technical assessment.
