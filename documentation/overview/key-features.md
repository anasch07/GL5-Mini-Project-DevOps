# Key Features

This project showcases the integration of a modern **DevOps pipeline** with a **FastAPI-based web application**. Below are the key features of this project:

## 1. **RESTful API Implementation**
- Built with **FastAPI**, a high-performance framework.
- Provides clean, well-documented endpoints for task management.
- Includes models, routes, and services for scalability and maintainability.

## 2. **Containerized Deployment**
- Fully containerized using **Docker** for consistency across environments.
- **Docker Compose** orchestrates multiple services (application, database, SonarQube).

## 3. **Automated CI/CD Pipeline**
- Built with **GitHub Actions** to automate:
  - Linting and formatting with **ruff**.
  - Unit testing and coverage reporting with **pytest**.
  - Vulnerability scanning using **Trivy**.
  - Code quality analysis with **SonarQube**.
  - Building and pushing Docker images to **DockerHub**.

## 4. **Code Quality Assurance**
- **SonarQube** integration to analyze:
  - Code smells.
  - Bugs and vulnerabilities.
  - Maintainability metrics.
- Configured to block the pipeline if critical issues are found.

## 5. **Vulnerability Scanning**
- Integrates **Trivy** to scan:
  - Application source code for security vulnerabilities.
  - Docker images for outdated dependencies and CVEs.
- Ensures high security standards in the DevOps pipeline.

## 6. **Database Management**
- **PostgreSQL** as the database with persistent storage.
- **Alembic** used for database migrations.
- Ensures data integrity and version control.


## 7. **Comprehensive Documentation**
- Clear and concise project documentation covering:
  - Setup and prerequisites.
  - CI/CD workflows and job breakdowns.
  - Instructions for local and Dockerized deployment.
