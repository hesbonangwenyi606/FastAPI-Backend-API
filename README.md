FastAPI Backend API

A RESTful backend API built with FastAPI, integrating PostgreSQL, SQLAlchemy, and Pydantic.
This project demonstrates backend development best practices — including authentication, CRUD operations, and database models.

Tech Stack

FastAPI — High-performance web framework for APIs

PostgreSQL — Relational database

SQLAlchemy — ORM for database models

Pydantic — Data validation and settings management

Uvicorn — ASGI server to run FastAPI apps

Docker & Docker Compose — Containerized environment

Features

CRUD operations for users and other entities

JWT authentication and authorization

Data validation with Pydantic schemas

PostgreSQL database integration

Auto-generated API docs via Swagger UI and ReDoc

Project Structure
FastAPI-Backend-API/
│
├── app/
│   ├── main.py          # Entry point
│   ├── routes/          # API routes
│   ├── models/          # Database models
│   ├── schemas/         # Pydantic schemas
│   └── database.py      # DB configuration
│
├── .env.example         # Example environment variables
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image build instructions
├── docker-compose.yml   # Docker Compose stack
├── README.md            # Project documentation
└── .gitignore           # Git ignore rules

Setup Instructions
1. Clone the repository
git clone https://github.com/hesbonangwenyi606/FastAPI-Backend-API.git
cd FastAPI-Backend-API

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables

Create a .env file in the project root (copy from example):

cp .env.example .env


Example .env:

DATABASE_URL=postgresql://username:password@localhost/db_name
SECRET_KEY=your-secret-key

Running the Server
Development (local)
uvicorn app.main:app --reload


Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Docker (recommended)

Build and start services:

docker compose up -d --build


Follow logs:

docker compose logs -f


Stop services:

docker compose down

Example API Request

GET /api/users

Response:

[
  {
    "id": 1,
    "username": "hesbon",
    "email": "hesbon@example.com"
  }
]

Contributing

Fork the repository

Create a new branch:

git checkout -b feature-branch


Commit your changes:

git commit -m 'Add new feature'


Push to your branch:

git push origin feature-branch


Open a Pull Request

License

This project is open-source and available under the MIT License.

.gitignore
# Virtual environment
venv/
ENV/

# Python cache files
__pycache__/
*.py[cod]
*$py.class

# Environment variables
.env
.env.*

# Database files
*.sqlite3
*.db

# IDE and system files
.idea/
.vscode/
.DS_Store

# Logs
*.log

# Byte-compiled / optimized files
*.pyo
*.pyd
*.pdb

# Test and coverage
htmlcov/
.coverage
.tox/
.pytest_cache/

# Misc
*.egg-info/
dist/
build/