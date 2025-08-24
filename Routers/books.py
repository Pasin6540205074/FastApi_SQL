from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from DB.models import Book, User
from DB.schemas import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["หนังสือ"])

@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, owner_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == owner_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="ไม่พบผู้ใช้งานเจ้าของหนังสือ")
    db_book = Book(**book.dict(), owner_id=owner_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=list[BookResponse])
def read_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@router.get("/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="ไม่พบบันทึกหนังสือ")
    return book

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, updated: BookCreate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="ไม่พบบันทึกหนังสือ")
    book.title = updated.title
    book.author = updated.author
    db.commit()
    db.refresh(book)
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="ไม่พบบันทึกหนังสือ")
    db.delete(book)
    db.commit()
    return {"message": "ลบหนังสือสำเร็จ"}
