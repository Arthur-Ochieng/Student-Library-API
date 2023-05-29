from fastapi import APIRouter, HTTPException, Depends
import schemas
import crud
from sqlalchemy.orm import Session
from dependencies import get_db

router = APIRouter(
    prefix="/book",
    tags=["book"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate,  db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@router.get("/books", response_model=list[schemas.Book])
def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _book = crud.get_books(db, skip=skip, limit=limit)
    return _book


@router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    _book = crud.get_book(db, book_id=book_id)
    if _book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return _book

@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    _book = crud.update_book(book_id, book, db)
    if _book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return _book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    crud.delete_book(db, book_id=book_id)
    return {"message": "Book deleted successfully"}


