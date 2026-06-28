from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.job import Job
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SEO Analyzer API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    router,
    prefix="/api"
)


@app.get("/")
def home():
    return {
        "message": "SEO Analyzer API Running"
    }