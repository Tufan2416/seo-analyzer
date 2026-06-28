from sqlalchemy import Column, String, Text

from app.database.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(String, primary_key=True, index=True)

    status = Column(String)

    result = Column(Text)