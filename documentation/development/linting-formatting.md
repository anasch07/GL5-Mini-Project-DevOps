# Linting and Formatting Guide

Maintaining code quality is crucial for ensuring readability, maintainability, and consistency across the project. This project employs the following tools for linting and formatting:

---

## Tools Used

### 1. **Ruff**
   - A fast and configurable Python linter.
   - Checks for coding standards, unused imports, and other common issues.

### 2. **Black**
   - A Python code formatter.
   - Ensures a consistent code style across the project.

### 3. **isort**
   - Organizes and formats imports according to the defined project style.

### 4. **Pre-Commit**
   - A framework for managing and running hooks before committing changes.

---

## Configuration Details

### Poetry Configuration (`pyproject.toml`)
- The project's `pyproject.toml` contains the necessary dependencies and tool configurations:

#### **Dependencies**
```toml
[tool.poetry.dependencies]
ruff = "^0.0.289"
flake8 = "^6.0.0"
isort = "^5.13.2"
pre-commit = "4.0.1"
```

#### **isort Configuration**
```toml
[tool.isort]
profile = "black"
skip = ["alembic/env.py", "alembic/versions"]
line-length = 120
exclude = ["alembic/versions/*.py", "alembic/env.py"]
```

#### **Ruff Configuration**
```toml
select = [
    "E",    # pycodestyle
    "W",    # pycodestyle
    "F",    # pyflakes
    "I",    # isort
    "B",    # flake8-bugbear
    "C4",   # flake8-comprehensions
    "UP"    # pyupgrade
]
ignore = []
```

---

### Pre-Commit Hooks Configuration (`.pre-commit-config.yaml`)
- Ensures hooks are run automatically before committing code:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.2
    hooks:
      - id: ruff
        args: ["--fix"]
        exclude: "alembic/versions/.*.py"

  - repo: https://github.com/psf/black
    rev: 23.9.1
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort
        exclude: "alembic/versions/.*.py"
```

---

## How to Use Linting and Formatting Tools

### 1. **Running Ruff**
- Check for linting issues:
  ```bash
  poetry run ruff .
  ```
- Automatically fix issues:
  ```bash
  poetry run ruff . --fix
  ```

### 2. **Running Black**
- Format the codebase:
  ```bash
  poetry run black .
  ```

### 3. **Running isort**
- Organize imports:
  ```bash
  poetry run isort .
  ```

### 4. **Pre-Commit Hooks**
- Install hooks to automatically lint and format code before commits:
  ```bash
  poetry run pre-commit install
  ```

- Manually run hooks:
  ```bash
  poetry run pre-commit run --all-files
  ```

---

## Ignored Files and Directories

Certain files and directories are excluded from linting and formatting to prevent unnecessary changes:
- `alembic/env.py`
- Files in `alembic/versions/`

These exclusions are defined in both the `pyproject.toml` and `.pre-commit-config.yaml`.

---

## Integrating with CI/CD

The CI/CD pipeline automatically runs linting and formatting as part of the workflow. If issues are detected, the pipeline fails, prompting developers to resolve them locally.

---

### Summary of Commands
| Command                        | Description                          |
|--------------------------------|--------------------------------------|
| `poetry run ruff .`            | Check for linting issues            |
| `poetry run ruff . --fix`      | Fix linting issues                  |
| `poetry run black .`           | Format code with Black              |
| `poetry run isort .`           | Organize imports with isort         |
| `poetry run pre-commit install`| Install pre-commit hooks            |
| `poetry run pre-commit run`    | Run pre-commit hooks on all files   |

