from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Module-level variable for dependency injection
db_dependency = Depends(get_db)


@app.get("/tasks", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = db_dependency):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = db_dependency):
    return crud.create_task(db=db, task=task)
