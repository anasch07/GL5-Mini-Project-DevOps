### **Security Scan**

#### **Trivy**
- Trivy scans the project for vulnerabilities, focusing on critical and high-severity issues.
- The pipeline fails if unresolved vulnerabilities are found.

**Example Trivy Command:**
```bash
trivy fs ./fastapi-docker-app \
  --severity CRITICAL,HIGH \
  --exit-code 1 \
  --ignore-unfixed \
  --format table
```

---

