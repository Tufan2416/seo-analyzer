import json
import uuid

from sqlalchemy.orm import Session

from app.models.job import Job


def create_job(db: Session):

    job_id = str(uuid.uuid4())

    job = Job(
        id=job_id,
        status="processing",
        result=""
    )

    db.add(job)
    db.commit()

    return job_id


def update_job(db: Session, job_id, report):

    job = db.query(Job).filter(Job.id == job_id).first()

    if job:

        job.status = "completed"

        job.result = json.dumps(report)

        db.commit()


def get_job(db: Session, job_id):

    return db.query(Job).filter(Job.id == job_id).first()