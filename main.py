from fastapi import FastAPI
from database import engine, Base
from Routers import users, books

# สร้างตารางอัตโนมัติ
Base.metadata.create_all(bind=engine)

app = FastAPI(title="โปรเจกต์ FastAPI ผู้ใช้งานและหนังสือ")

# เพิ่ม routers
app.include_router(users.router)
app.include_router(books.router)

@app.get("/")
def root():
    return {"ข้อความ": "ยินดีต้อนรับเข้าสู่ระบบจัดการผู้ใช้งานและหนังสือ"}
