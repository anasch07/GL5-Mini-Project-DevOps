# FastAPI Task Management API with DevOps Pipeline

## Overview

This project is a **Task Management API** built using **FastAPI**. It features a containerized setup with **Docker** and integrates a robust CI/CD pipeline. The goal is to provide hands-on experience with modern DevOps practices while delivering a scalable and maintainable application.

---

## Goal of this TP

This project aims to:

- Demonstrate how to set up and configure a complete DevOps pipeline.
- Incorporate tools like **SonarQube** for code quality and **Trivy** for vulnerability scanning.
- Automate testing, linting, formatting, and deployment processes.
- Provide practical exposure to CI/CD tools such as **GitHub Actions**.

---

## Setup

### Prerequisites

1. Install **Docker** and **Docker Compose**:
   - [Get Docker](https://www.docker.com/get-started)
   - [Install Docker Compose](https://docs.docker.com/compose/install/)

2. **Set up SonarQube server**:
   - Use the following `docker-compose.yml` to deploy a local SonarQube server:
     ```yaml
     version: "3"
     services:
       sonarqube:
         image: sonarqube:latest
         container_name: sonarqube
         ports:
           - "9000:9000"
         volumes:
           - sonarqube_data:/opt/sonarqube/data
           - sonarqube_logs:/opt/sonarqube/logs
           - sonarqube_extensions:/opt/sonarqube/extensions
     volumes:
       sonarqube_data:
       sonarqube_logs:
       sonarqube_extensions:
     ```

   - Run the server:
     ```bash
     docker-compose up -d
     ```

   - Access SonarQube at `http://localhost:9000`.

3. Generate a **SonarQube token** for CI/CD integration.

---

## Installation

### Local Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd fastapi-docker-app
   ```

2. Install dependencies:
   ```bash
   pip install poetry
   poetry install
   ```

3. Run the development server:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

### Dockerized Installation

1. Build and start the application:
   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://localhost:8000`.

---

## Directory Structure

```
fastapi-docker-app/
├── app/
│   ├── main.py           # Entry point of the application
│   ├── models.py         # Database models
│   └── routes.py         # API routes
├── tests/                # Test cases
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── pyproject.toml        # Poetry configuration
└── README.md             # Documentation
```

---

## Development Guide

### Linting and Formatting

This project uses **ruff** for linting and formatting.

- To check for issues:
  ```bash
  poetry run ruff .
  ```

- To fix issues automatically:
  ```bash
  poetry run ruff . --fix
  ```

### Writing and Running Tests

Unit tests are written using **pytest**.

- Run all tests:
  ```bash
  poetry run pytest
  ```

- Generate a coverage report:
  ```bash
  poetry run pytest --cov=app
  ```

---

## CI/CD Workflow Overview

### Pipeline Overview

This project uses **GitHub Actions** to automate the CI/CD pipeline.

### Jobs Breakdown

#### 1. Lint, Format, Test
- Runs `ruff` for linting and formatting.
- Executes `pytest` for unit tests.

#### 2. Security Scan (Trivy)
- Scans the codebase and Docker image for vulnerabilities.

#### 3. Code Quality (SonarQube)
- Analyzes code quality metrics and generates reports in SonarQube.

#### 4. Build and Push Docker Image
- Builds a Docker image for the application.
- Pushes the image to DockerHub.

---

## Security and Quality

### Vulnerability Scanning with Trivy

- Trivy scans the source code and Docker images for vulnerabilities.
- Output includes critical and high-severity vulnerabilities.

### Code Quality Metrics with SonarQube

- Identifies bugs, code smells, and security vulnerabilities.
- Provides actionable recommendations for code improvement.

---

## Deployment

### Docker Image Build and Push

- Docker image is built and pushed to **DockerHub** as part of the pipeline.

### Running the Application with Docker

- Start the application:
  ```bash
  docker-compose up
  ```

- Stop the application:
  ```bash
  docker-compose down
  ```

---

## Contributing

### Contribution Guidelines

1. Fork the repository and create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```

2. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```

3. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```

4. Create a pull request.

### Pull Request and Code Review Process

- Ensure all tests pass before submitting a pull request.
- Address feedback from reviewers promptly.
- Follow the coding standards defined in the project.

