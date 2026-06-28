
from pydantic import BaseModel

from app.services.seo_service import generate_report
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.crud import create_job, update_job, get_job
router = APIRouter()


class AnalyzeRequest(BaseModel):
    url: str


@router.post("/analyze")
def analyze(request: AnalyzeRequest, db: Session = Depends(get_db)):

    job_id = create_job(db)

    report = generate_report(request.url)

    update_job(db, job_id, report)

    return {
        "job_id": job_id,
        "status": "completed"
    }

@router.get("/results/{job_id}")
def results(
    job_id: str,
    db: Session = Depends(get_db)
):

    job = get_job(db, job_id)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    import json

    return {
    "job_id": job.id,
    "status": job.status,
    "result": json.loads(job.result) if job.result else None
}