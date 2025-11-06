# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Try to get DATABASE_URL from .env, otherwise fallback to default MySQL container settings
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:password@laravel-db:3306/mydb"  # fallback for Docker
)

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # helps avoid "MySQL server has gone away" errors
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
