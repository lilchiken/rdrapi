from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import postgres


engine = create_engine(
    postgres
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=True,
    autoflush=True
)

Base = declarative_base()

def get_db() -> Generator:
    """Dependency for getting async session."""

    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()