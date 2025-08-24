from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ใช้ SQLite เป็นฐานข้อมูล
DATABASE_URL = "sqlite:///./DB/database.db"

# ถ้าอยากใช้ PostgreSQL แก้ตรงนี้ เช่น
# DATABASE_URL = "postgresql://user:password@localhost:5432/mydatabase"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency สำหรับเชื่อมต่อ DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
