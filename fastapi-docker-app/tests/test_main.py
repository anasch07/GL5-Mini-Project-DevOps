import os
import sys

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.main import app, get_db  # Move these to the top

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# fixture to clean up the database after tests
@pytest.fixture(scope="module", autouse=True)
def teardown():
    yield
    # drop the test database tables after tests
    Base.metadata.drop_all(bind=engine)
    # remove the test database file
    os.remove("./test.db")


def test_create_task():
    response = client.post(
        "/tasks", json={"name": "Test Task", "completion_status": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Task"
    assert not data["completion_status"]
    assert "id" in data
    assert data["id"] == 1


def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["name"] == "Test Task"
    assert not data[0]["completion_status"]
