from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    completion_status = Column(Boolean, default=False)
