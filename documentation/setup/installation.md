# Installation

This guide provides step-by-step instructions to install and run the application both locally and in a Dockerized environment.

---

## Local Installation

To set up the application on your local machine, follow these steps:

### 1. Clone the Repository
First, clone the project repository to your local system:
```bash
git clone https://github.com/anasch07/GL5-Mini-Project-DevOps.git

cd GL5-Mini-Project-DevOps/fastapi-docker-app
```

### 2. Install Dependencies
This project uses **Poetry** for dependency management. Install Poetry if you haven't already:
```bash
pip install poetry
```

Then, install the project's dependencies:
```bash
poetry install
```

### 3. Run the Application Locally
Start the FastAPI application:
```bash
cd fastapi-docker-app
poetry run uvicorn app.main:app --reload
```

The application will be accessible at:
```
http://localhost:8000
```

### 4. (Optional) Run Tests Locally
To verify that everything works correctly, run the unit tests:
```bash
cd fastapi-docker-app
poetry run pytest
```

---

## Dockerized Installation

For a production-ready setup or easier deployment, you can run the application in a Dockerized environment.

### 1. Build and Start the Application
Navigate to the project root directory and run the following command:
```bash
docker-compose up --build
```

This command will:
- Build the Docker image for the FastAPI application.
- Start both the **FastAPI app** and **PostgreSQL database** containers as defined in the `docker-compose.yml`.

### 2. Access the Application
Once the containers are running, you can access the application at:
```
http://localhost:8000
```

### 3. Stopping the Application
To stop the running containers, execute:
```bash
docker-compose down
```

This will:
- Stop the running containers.
- Preserve the PostgreSQL database data in a Docker volume.

---



## Notes on Dockerized Installation

- **Persistent Data**:
  - The database uses a named volume (`postgres_data`) to persist data. This means your database data will remain intact even after stopping and restarting the containers.

- **Configuration Files**:
  - Modify the `docker-compose.yml` file to change environment variables, ports, or service configurations.

- **Ports**:
  - The default application port is `8000`.
  - Ensure the port is not being used by other services.