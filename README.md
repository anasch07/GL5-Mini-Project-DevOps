# Updated Directory Structure

The directory structure for the **GL5-Mini-Project-DevOps** project has been updated. Below is the revised structure with descriptions of key components.

---

## Root Directory Structure

```
GL5-Mini-Project-DevOps/
├── Makefile                     # Automates tasks like building, testing, and running containers
├── README.md                    # Main project documentation
├── app/                         # Kubernetes deployment and service configuration
│   ├── deployment.yaml          # Deployment configuration for the application
│   └── service.yaml             # Service configuration for exposing the application
├── documentation/               # Detailed project documentation
│   ├── README.md                # Documentation main page
│   ├── SUMMARY.md               # Table of contents for GitBook structure
│   ├── cicd/                    # CI/CD pipeline documentation
│   ├── contributing/            # Contribution guidelines
│   ├── deployment/              # Deployment instructions
│   ├── development/             # Development guidelines
│   ├── overview/                # Project overview and features
│   ├── security-quality/        # Security and code quality documentation
│   └── setup/                   # Setup instructions and prerequisites
├── docker-compose.yml           # Main Docker Compose file for the FastAPI app and database
├── docker-compose-sonarQube.yml # Docker Compose file for SonarQube setup
├── fastapi-docker-app/          # Main FastAPI application
├── main-application.yaml        # Monitoring configuration for the main application
├── monitoring/                  # Monitoring and observability configuration
│   └── prometheus-values.yaml   # Prometheus configuration values
├── monitoring-application.yaml  # Application-level monitoring configuration
└── sonar-project.properties     # SonarQube configuration file for code analysis
```

---

## FastAPI Application Directory

```
fastapi-docker-app/
├── Dockerfile                   # Docker configuration for the FastAPI application
├── alembic.ini                  # Alembic configuration for database migrations
├── pyproject.toml               # Poetry configuration for dependencies
├── poetry.lock                  # Locked dependency versions
├── sonar-project.properties     # SonarQube configuration file
├── alembic/                     # Directory for database migrations
│   ├── env.py                   # Alembic environment setup
│   ├── script.py.mako           # Template for migration scripts
│   └── versions/                # Directory for individual migration scripts
├── app/                         # Core application logic
│   ├── __init__.py              # Package initializer
│   ├── main.py                  # Application entry point
│   ├── models.py                # Database models
│   ├── routes.py                # API route definitions
│   └── config.py                # Configuration for environment variables and database
├── tests/                       # Unit and integration tests
│   ├── __init__.py              # Package initializer
│   ├── test_main.py             # Tests for application routes and functionality
│   └── test_models.py           # Tests for database models
```

---

