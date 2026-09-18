"""
Database Connection Module
reads DATABASE_URL from the environment (via .env) so the same code runs
against SQLite for local development and MySQL in
production, without changing any application code.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./attendance.db")

# check_same_thread is only needed for SQLite
# threads for a single request/response cycle.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    API dependency that yields a DB session and always closes it
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
