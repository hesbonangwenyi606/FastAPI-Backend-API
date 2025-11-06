# 🚀 FastAPI Backend API

A RESTful backend API built with **FastAPI**, integrating **PostgreSQL**, **SQLAlchemy**, and **Pydantic**.  
This project is designed to demonstrate backend development best practices — including authentication, CRUD operations, and database models.

---

## 🔧 Tech Stack

- **FastAPI** — High-performance web framework for building APIs
- **PostgreSQL** — Relational database
- **SQLAlchemy** — ORM for database models
- **Pydantic** — Data validation and settings management
- **Uvicorn** — ASGI server for running FastAPI apps

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/hesbonangwenyi606/FastAPI-Backend-API.git
cd FastAPI-Backend-API
2. Create a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Linux or macOS
venv\Scripts\activate      # On Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Set up environment variables
Create a .env file in the project root based on the example below:

bash
Copy code
DATABASE_URL=postgresql://username:password@localhost/db_name
SECRET_KEY=your-secret-key
Alternatively, you can copy the example:

bash
Copy code
cp .env.example .env
5. Run the development server
bash
Copy code
uvicorn app.main:app --reload
📁 Project Structure
bash
Copy code
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
├── README.md            # Documentation
└── .gitignore           # Git ignore rules
🌍 API Docs
Once running, visit:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🧪 Example Request
bash
Copy code
GET /api/users
Response:

json
Copy code
[
  {
    "id": 1,
    "username": "hesbon",
    "email": "hesbon@example.com"
  }
]
🤝 Contributing
Fork the repo

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature-branch)

Open a Pull Request

🪪 License
This project is open-source and available under the MIT License.

yaml
Copy code

---

## 🛡️ **.gitignore**

```gitignore
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