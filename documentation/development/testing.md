# Writing and Running Tests

Testing is a critical aspect of any development process to ensure the application behaves as expected and maintains a high level of reliability. This guide details the testing strategy used for this project.

---

## Testing Framework

This project uses **pytest** for unit testing and integration testing. The tests ensure the application:

- Meets its functional requirements.
- Handles edge cases effectively.
- Maintains code quality over time.

---

## Test Setup and Configuration

### Database Configuration for Tests

During testing, the application uses an in-memory SQLite database to ensure tests are isolated and do not affect the production or development databases.

### Test Dependencies

The application’s dependencies and database session are overridden for testing. The `override_get_db` function ensures the test database is used during the tests.

---

### Test Code Structure

#### File Location
- Test files are located in the `tests` directory.
- Each test file matches the module it tests.

#### Sample Test File: `test_tasks.py`

```python
import os
import sys
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.main import app, get_db  # Import FastAPI app and database dependencies

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SQLite test database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create database schema for tests
Base.metadata.create_all(bind=engine)

# Override the database dependency for testing
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


# Fixture to clean up the database after tests
@pytest.fixture(scope="module", autouse=True)
def teardown():
    yield
    # Drop the test database tables after tests
    Base.metadata.drop_all(bind=engine)
    # Remove the test database file
    os.remove("./test.db")


# Unit Test: Test task creation
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


# Integration Test: Test retrieving tasks
def test_read_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["name"] == "Test Task"
    assert not data[0]["completion_status"]
```

---

## Running Tests

1. **Install Testing Dependencies**
   Ensure all dependencies are installed:
   ```bash
   poetry install
   ```

2. **Run Tests**
   Execute all tests using `pytest`:
   ```bash
   poetry run pytest
   ```

3. **View Test Coverage**
   Generate a coverage report to evaluate the extent of code tested:
   ```bash
   poetry run pytest --cov=app --cov-report=term-missing
   ```

---

## Key Features of the Test Suite

- **Database Isolation**:
  - Uses an in-memory SQLite database for testing.
  - The database schema is recreated for each test run.
  - The database file is removed after tests are completed.

- **Dependency Injection**:
  - Overrides `get_db` to inject the test database into the application during tests.

- **Teardown Mechanism**:
  - Ensures cleanup after tests by dropping tables and removing the SQLite test database file.

---

## Common Testing Commands

| Command                         | Description                          |
|---------------------------------|--------------------------------------|
| `poetry run pytest`             | Run all tests                       |
| `poetry run pytest --cov=app`   | Run tests and generate coverage      |
| `poetry run pytest -k test_name`| Run a specific test by its name      |
