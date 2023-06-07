# # from fastapi.testclient import TestClient

# # from main import app
# # client = TestClient(app)

# from fastapi.testclient import TestClient
# from sqlalchemy.orm import Session
# from unittest.mock import MagicMock
# from main import app
# from dependencies import get_db
# from crud import create_book, get_books, get_book, update_book, delete_book

# client = TestClient(app)


# def test_create_book(monkeypatch, db_session: Session):
#     # Mock the create_book function
#     mock_create_book = MagicMock(return_value={"id": 1, "title": "Book Title"})
#     monkeypatch.setattr("crud.create_book", mock_create_book)

#     # Send a POST request to the /book/ endpoint
#     response = client.post("/book/", json={"title": "Book Title"})

#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "title": "Book Title"}

#     # Verify that the create_book function was called with the correct arguments
#     mock_create_book.assert_called_once_with(db=db_session, book={"title": "Book Title"})


# def test_get_books(monkeypatch, db_session: Session):
#     # Mock the get_books function
#     mock_get_books = MagicMock(return_value=[{"id": 1, "title": "Book 1"}, {"id": 2, "title": "Book 2"}])
#     monkeypatch.setattr("crud.get_books", mock_get_books)

#     # Send a GET request to the /book/books endpoint
#     response = client.get("/book/books")

#     assert response.status_code == 200
#     assert response.json() == [{"id": 1, "title": "Book 1"}, {"id": 2, "title": "Book 2"}]

#     # Verify that the get_books function was called with the correct arguments
#     mock_get_books.assert_called_once_with(db=db_session, skip=0, limit=100)


# def test_get_book(monkeypatch, db_session: Session):
#     # Mock the get_book function
#     mock_get_book = MagicMock(return_value={"id": 1, "title": "Book Title"})
#     monkeypatch.setattr("crud.get_book", mock_get_book)

#     # Send a GET request to the /book/{book_id} endpoint
#     response = client.get("/book/1")

#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "title": "Book Title"}

#     # Verify that the get_book function was called with the correct arguments
#     mock_get_book.assert_called_once_with(db=db_session, book_id=1)


# def test_update_book(monkeypatch, db_session: Session):
#     # Mock the update_book function
#     mock_update_book = MagicMock(return_value={"id": 1, "title": "Updated Book Title"})
#     monkeypatch.setattr("crud.update_book", mock_update_book)

#     # Send a PUT request to the /book/{book_id} endpoint
#     response = client.put("/book/1", json={"title": "Updated Book Title"})

#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "title": "Updated Book Title"}

#     # Verify that the update_book function was called with the correct arguments
#     mock_update_book.assert_called_once_with(book_id=1, book={"title": "Updated Book Title"}, db=db_session)


# def test_delete_book(monkeypatch, db_session: Session):
#     # Mock the delete_book function
#     mock_delete_book = MagicMock()
#     monkeypatch.setattr("crud.delete_book", mock_delete_book)

#     # Send a DELETE request to the /book/{book_id} endpoint

