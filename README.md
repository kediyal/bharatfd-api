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

## 📸 Images

Here are some screenshots showcasing different features and views of the project:

- **FAQ Model View**
  A view of the `FAQ` model, displaying the structure and attributes of the FAQs.
  ![FAQ Model View](https://i.postimg.cc/8C5zXw4Q/faq-model-view.jpg)

- **FAQ Translation Model**
  The `FAQ Translation` model, highlighting the translations associated with each FAQ.
  ![FAQ Translation Model](https://i.postimg.cc/fy4WLsND/faq-translation-model.jpg)

- **Redis Cache: English (en)**
  Cached data for English (`en`) in Redis, where the FAQs are stored.
  ![Redis Cache - English](https://i.postimg.cc/bYbN5ZxJ/redis-en-cache.jpg)

- **Redis Keys**
  A list of all keys currently stored in Redis, with their corresponding values.
  ![Redis Keys](https://i.postimg.cc/MTfKqTg9/redis-keys.jpg)

- **Rich Text Formatting (RTF) Content**
  A view of the rich text formatting (RTF) editor used in the application, showing how content is formatted.
  ![RTF Content](https://i.postimg.cc/5tRNhvKH/rtf-ck.jpg)

- **Swagger API Documentation**
  The API documentation interface generated using Swagger, which allows users to explore and test the API endpoints.
  ![Swagger API Documentation](https://i.postimg.cc/brQyS5yb/swagger.jpg)

- **Swagger - GET Endpoint (English)**
  The GET request for the English FAQ data via the Swagger API interface.
  ![Swagger GET - English](https://i.postimg.cc/X7b76nLg/swagger-get-en.jpg)

- **Swagger - GET Endpoint (Hindi)**
  The GET request for the Hindi FAQ data via the Swagger API interface.
  ![Swagger GET - Hindi](https://i.postimg.cc/287jzgXN/swagger-get-hi.jpg)

- **Redoc API Documentation**
  The API documentation generated using Redoc, providing an alternative way to explore the API.
  ![Redoc API Documentation](https://i.postimg.cc/dtjW49D9/redoc.jpg)
  |

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

## 🧪 Unit Tests

We’ve added unit tests to ensure the core functionalities are working as expected. The tests cover the following areas:

- **TestFAQModel**: Ensures the `FAQ` model behaves as expected.
- **TestFAQTranslationModel**: Verifies the correct functioning of the `FAQTranslation` model.
- **TestCaching**: Tests the caching system with Redis to ensure it stores and retrieves FAQs correctly.

### Test Runthrough

Here’s a quick demo showing the unit tests in action:

![Unit Tests Runthrough](https://i.postimg.cc/yxyBmby5/unit-tests-runthrough.gif)

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
