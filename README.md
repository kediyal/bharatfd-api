# BharatFD FAQ API 🚀

This is a fast, scalable, and multilingual FAQ management system built with Django. It features instant translations, efficient caching, and a smooth admin experience. Let's dive in!

---

## 🔥 Features

- **Two-Model Design**️: Instead of stuffing translations into a single model, we use `FAQ` and `FAQTranslation`, making it super easy to scale.
- **Instant Translations**: New FAQs automatically get translated using `googletrans`, handling async/sync calls efficiently.
- **Redis Caching** Cached translations (both individual and list-based) for faster responses.
- **Beautiful Admin Panel**: Clean UI with language filters, date filters, and search.
- **WYSIWYG Editor**: CKEditor integration for rich text editing.
- **Fully Documented API**: Interactive docs via Swagger and ReDoc.

---

## 🚀 Quick Start

### 1️⃣ Installation

```bash
# Clone the repo
git clone https://github.com/kediyal/bharatfd-api.git && cd bharatfd-api

# Create a virtual environment
python -m venv venv && source venv/bin/activate  # (or venv\Scripts\activate on Windows)

# Install dependencies from the root-level requirements.txt
pip install -r requirements.txt

# Navigate to the backend directory
cd backend

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

---

### 2️⃣ API Documentation

- **Swagger UI**: [http://localhost:8000/swagger-ui/](http://localhost:8000/swagger/)
- **ReDoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

### 3️⃣ API Endpoints

#### Fetch FAQs

```bash
# Default (English)
curl http://localhost:8000/api/faqs/

# Hindi
curl http://localhost:8000/api/faqs/?lang=hi

# Bengali
curl http://localhost:8000/api/faqs/?lang=bn
```

---

## 📸 Screenshots (Coming Soon)

Stay tuned! 🚀

---

## ⚙️ Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Caching:** Redis
- **Translation:** googletrans
- **Docs:** Swagger, ReDoc
- **Admin Panel:** Django Admin + CKEditor

---

## 🏗️ To-Do (Upcoming Features)

- [ ] Unit tests using `pytest`
- [ ] Docker setup for easy deployment
- [ ] CI/CD pipeline

---

# 🛠️ Code Quality & Automation

We use pre-commit hooks to maintain high code quality and ensure that commits follow a consistent format.

### Pre-Commit Hooks

Pre-commit hooks automatically run before each commit to check for common issues and enforce standards. Here’s what we check for:

- **Whitespace**: Automatically removes trailing spaces at the end of lines.
- **File Formatting**: Ensures files end with a newline and are properly formatted.
- **Linter**: Runs _Ruff_, a fast linter that checks Python code for style and potential bugs.
- **Conventional Commits**: Uses _Commitizen_ to make sure your commit messages follow the conventional commits format.

### Setting Up Locally

To get started with the pre-commit hooks:

1. Install pre-commit (if you haven’t already):

   ```bash
   pip install pre-commit
   ```

2. Install the hooks:

   ```bash
   pre-commit install
   ```

3. Optionally, run the hooks manually:
   ```bash
   pre-commit run --all-files
   ```

To keep everything up to date, you can also run:

```bash
pre-commit autoupdate
```

### Python Project Settings

This project is set up with the following configurations:

- **Python Version**: We’re using Python 3.12.4.
- **Ruff Linter**: Configured with Pyflakes rules and security checks.
- **Commitizen**: For generating consistent version tags and changelogs.

Here’s a snapshot of the configuration files for _ruff_ and _commitizen_:

```toml
[tool.ruff]
line-length = 79
select = ["F", "E4", "E7", "E9", "W", "S", "I", "B", "SIM"]
fixable = ["ALL"]

[tool.commitizen]
name = "cz_conventional_commits"
tag_format = "v0.0.1"
version_scheme = "pep440"
version_provider = "pep621"
update_changelog_on_bump = true
major_version_zero = true
```

---

## 🛠️ Contributing

Want to improve this? PRs are welcome! Just follow these steps:

```bash
# Fork the repo
# Create a new branch
git checkout -b feature-branch

# Make your changes and commit
git commit -m "feat: add cool feature"

# Push and create a PR
git push origin feature-branch
```

---

### 🎯 Ready? Run it and test the API now! 🚀
