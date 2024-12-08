# Prerequisites

To get started, ensure you have the following installed:

1. **Docker**: [Get Docker](https://www.docker.com/get-started)
2. **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
3. **SonarQube Server**:
   - Set up SonarQube locally using the `docker-compose-sonarQube.yml` file:
     ```bash
     docker-compose -f docker-compose-sonarQube.yml up -d
     ```
   - Access SonarQube at `http://localhost:9000` and generate a token for CI/CD integration.