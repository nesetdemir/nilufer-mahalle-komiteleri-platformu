from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Veritabanı engine'i oluştur
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model sınıfı
Base = declarative_base()


# Dependency injection için session getter
def get_db():
    """
    Veritabanı session'ı sağlar.
    FastAPI dependency injection için kullanılır.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

