from pydantic import BaseModel, EmailStr

# ------------------- USER -------------------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True   # แก้จาก orm_mode

# ------------------- BOOK -------------------
class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    owner_id: int
    class Config:
        from_attributes = True   # แก้จาก orm_mode
