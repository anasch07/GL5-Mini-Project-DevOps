### **Jobs Breakdown**

#### **1. Lint**
- Ensures code adheres to defined linting standards using **ruff**.
- Validates that the code is error-free and follows style guidelines.

**Key Steps:**
1. Check out the code.
2. Set up Python (v3.10).
3. Install project dependencies.
4. Run `ruff` to lint the code.

#### **2. Format**
- Formats the codebase using **ruff** with automatic fixes.

**Key Steps:**
1. Check out the code.
2. Set up Python (v3.10).
3. Install project dependencies.
4. Run `ruff` with the `--fix` flag to apply formatting.

#### **3. Test**
- Executes unit tests written in **pytest**.
- Generates a coverage report for code quality.

**Key Steps:**
1. Check out the code.
2. Set up Python (v3.10).
3. Install test dependencies (e.g., `pytest`, `pytest-cov`).
4. Run tests with coverage reporting.
5. Upload the coverage report as an artifact for further analysis.

#### **4. Security Scan (Trivy)**
- Scans the source code for critical and high-severity vulnerabilities.
- Ensures no major vulnerabilities exist in the codebase or dependencies.

**Key Steps:**
1. Check out the code.
2. Install **Trivy**.
3. Run Trivy on the source code with strict severity checks (`CRITICAL`, `HIGH`).

#### **5. Code Quality (SonarQube)**
- Integrates **SonarQube** to analyze code quality and detect issues like bugs, code smells, and security vulnerabilities.
- Uses the SonarQube token and URL for authentication and connection.

**Key Steps:**
1. Check out the code.
2. Download the test coverage report.
3. Run the SonarQube scan using `sonarsource/sonarqube-scan-action`.

#### **6. Build and Push Docker Image**
- Builds a Docker image for the application.
- Pushes the image to DockerHub after all quality and security checks pass.

**Key Steps:**
1. Check out the code.
2. Set up Docker Buildx for efficient builds.
3. Build the Docker image.
4. Push the image to DockerHub.

---

