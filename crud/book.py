from fastapi import HTTPException
from sqlalchemy.orm import  Session  # Session = ตัวกลางในการคุยกับฐานข้อมูลผ่าน ORM model โดยปลอดภัยและมีการควบคุม transaction
from ..models import book as models
from ..schemas import book as schemas

def create_book(db:Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db:Session):
    return db.query(models.Book).all()

def get_book(db:Session, book_id:int):
    db_book =  db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book Not found")
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db:Session, book_id:int, book:schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        for key, value in book.model_dump().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book            
    
def delete_book(db:Session, book_id:int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    book_name = db_book.title
    db.delete(db_book)
    db.commit()
    return {"message": f"Book {book_name} deleted"}