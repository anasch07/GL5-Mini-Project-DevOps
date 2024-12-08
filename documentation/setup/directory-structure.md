# Directory Structure

This document outlines the structure of the project and provides a description of each directory and file.

---

## Project Root Structure

```
GL5-Mini-Project-DevOps/
├── Makefile                     # Automates common tasks like building, testing, and running containers
├── README.md                    # Main project documentation
├── SUMMARY.md                   # Table of contents for detailed documentation
├── docker-compose.yml           # Main Docker Compose file for the FastAPI app and database
├── docker-compose-sonarQube.yml # Docker Compose file for setting up SonarQube
├── main-application.yaml        # Monitoring configuration for the main app
├── monitoring/                  # Files related to monitoring and observability
├── sonar-project.properties     # SonarQube configuration file
├── documentation/               # Detailed project documentation
├── fastapi-docker-app/          # Main FastAPI application
└── app/                         # Application-level scripts and utilities
```

---

## FastAPI Application Directory Structure

```
fastapi-docker-app/
├── Dockerfile                   # Docker configuration for the FastAPI application
├── alembic.ini                  # Alembic configuration for database migrations
├── pyproject.toml               # Poetry configuration for dependencies
├── poetry.lock                  # Locked dependency versions
├── sonar-project.properties     # Configuration file for SonarQube analysis
├── alembic/                     # Database migrations
│   ├── env.py                   # Alembic environment setup
│   ├── script.py.mako           # Template for migrations
│   └── versions/                # Directory for individual migration scripts
├── app/                         # Core application logic
│   ├── __init__.py              # Package initializer
│   ├── main.py                  # Application entry point
│   ├── models.py                # Database models
│   ├── routes.py                # API route definitions
│   └── config.py                # Application configuration (database URL, environment variables, etc.)
├── tests/                       # Unit and integration tests
│   ├── __init__.py              # Package initializer
│   ├── test_main.py             # Tests for application routes and functionality
│   └── test_models.py           # Tests for database models
```

---

## Key Directories and Files

### 1. **Project Root**
- **`Makefile`**: Automates tasks such as running tests, building containers, and applying migrations.
- **`README.md`**: Provides an overview and setup instructions for the project.
- **`docker-compose.yml`**: Defines services for the FastAPI app and PostgreSQL database.
- **`docker-compose-sonarQube.yml`**: Deploys SonarQube for code quality analysis.
- **`sonar-project.properties`**: Configuration for SonarQube scans in the CI/CD pipeline.

### 2. **FastAPI Application (`fastapi-docker-app/`)**
- **`Dockerfile`**: Instructions to build a container for the FastAPI application.
- **`pyproject.toml`**: Poetry project configuration with metadata and dependencies.
- **`poetry.lock`**: Ensures consistency in installed dependencies.
- **`alembic/`**: Handles database migrations using Alembic.

### 3. **Application Code (`app/`)**
- **`main.py`**: Application entry point. Starts the FastAPI server.
- **`models.py`**: Defines database models.
- **`routes.py`**: Contains API route definitions.
- **`config.py`**: Centralizes configuration variables.

### 4. **Tests (`tests/`)**
- **Purpose**: Ensures application functionality and integrity.
- Includes test cases for routes (`test_main.py`) and database models (`test_models.py`).

