Module 13 – JWT Authentication, Client-Side Validation & Playwright E2E

This project implements JWT-based user registration and login, a minimal front-end for authentication, Playwright end-to-end tests, and a Docker-based CI/CD pipeline with GitHub Actions.

This module builds on earlier assignments by introducing a full authentication workflow (register → login → token verification) and validating it through automated tests.

🚀 Features
🔐 JWT Authentication (FastAPI)

/auth/register – Creates a new user

/auth/login – Validates credentials and returns a JWT

Passwords hashed with bcrypt

Pydantic validation for secure data handling

🌐 Front-End (HTML/CSS/JS)

register.html & login.html

Client-side validation:

Email format

Minimum password length

Password confirmation

Successful login → token stored in localStorage

🤖 Playwright E2E Tests

Covers:

Successful registration

Successful login

Error handling for:

invalid email

short password

mismatched passwords

incorrect login credentials

🛠️ CI/CD Pipeline (GitHub Actions)

Spins up PostgreSQL

Installs dependencies + browsers

Runs:

Unit tests

Integration tests

E2E tests

If ALL tests pass → pushes Docker image to Docker Hub

🐳 Docker Containerization

FastAPI app runs fully in Docker

PostgreSQL + pgAdmin4 supported

Ready for local or cloud deployment

📁 Project Structure
module13_is601/
│
├── app/
│   ├── auth/             # JWT logic, dependencies
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── main.py           # FastAPI entry point
│   ├── database.py       # DB connection
│   └── database_init.py  # Initial DB setup
│
├── static/
│   ├── login.html        # Front-end page
│   └── register.html     # Front-end page
│
├── tests/
│   ├── e2e/              # Playwright E2E tests
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
│
├── .github/workflows/
│   └── test.yml          # CI/CD workflow
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

🛠️ Local Setup (Without Docker)
1️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

2️⃣ Install Requirements
pip install --upgrade pip
pip install -r requirements.txt

3️⃣ Start FastAPI
uvicorn app.main:app --reload


API will be available at:

👉 http://127.0.0.1:8000

👉 http://127.0.0.1:8000/docs

🐳 Running With Docker
Build + Start
docker compose up --build


Services:

FastAPI → http://localhost:8000

PostgreSQL → localhost:5432

pgAdmin → http://localhost:5050

🌐 Using the Front-End

Open directly in your browser:

static/login.html
static/register.html


OR serve with a simple file server:

python -m http.server 8001

🤖 Running E2E Tests Locally
Install Playwright Browsers
playwright install
Run E2E Test
pytest tests/e2e/ -s -v


🔄 CI/CD — GitHub Actions

Workflow file: .github/workflows/test.yml

Pipeline steps:

Start PostgreSQL

Install dependencies

Run unit tests

Run integration tests

Run Playwright E2E tests

Build Docker image

Push to Docker Hub (on main branch)

🐳 Docker Hub Repo

Image pushes to:

msaju20/module13_is601:latest
msaju20/module13_is601:<commit_sha>



📝 Reflection Summary (Module Requirement)

This module strengthened skills in:

JWT authentication

Secure password hashing

Front-end validation

Playwright E2E automation

Debugging API + front-end flows

CI/CD pipelines

Docker-based application infrastructure

👩‍🏫 Instructor Expectations Checklist

✔ GitHub repo link
✔ Working JWT register/login
✔ Front-end pages with validation
✔ Passing Playwright tests screenshot
✔ Screenshot of CI/CD workflow passing
✔ Screenshot of Docker Hub push
✔ Reflection document