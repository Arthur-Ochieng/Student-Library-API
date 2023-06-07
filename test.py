import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database, database_exists

from main import app
from schemas import StudentCreate, StudentUpdate

# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    if database_exists(SQLALCHEMY_DATABASE_URL):
        drop_database(SQLALCHEMY_DATABASE_URL)
    create_database(SQLALCHEMY_DATABASE_URL)
    yield
    drop_database(SQLALCHEMY_DATABASE_URL)


client = TestClient(app)


def test_create_student():
    student_data = {
        "name": "John Doe",
        "age": 20,
        "grade": "A",
    }
    response = client.post("/student/", json=student_data)
    assert response.status_code == 200
    student = response.json()
    assert student["name"] == student_data["name"]
    assert student["age"] == student_data["age"]
    assert student["grade"] == student_data["grade"]
    assert "id" in student


def test_get_students():
    response = client.get("/student/students")
    assert response.status_code == 200
    students = response.json()
    assert isinstance(students, list)


def test_get_student():
    # Assuming there is a student with id=1 in the database
    response = client.get("/student/1")
    assert response.status_code == 200
    student = response.json()
    assert "name" in student
    assert "age" in student
    assert "grade" in student


def test_get_nonexistent_student():
    # Assuming there is no student with id=999 in the database
    response = client.get("/student/999")
    assert response.status_code == 404
    error = response.json()
    assert error["detail"] == "Student not found"


def test_update_student():
    # Assuming there is a student with id=1 in the database
    student_data = {
        "name": "Jane Smith",
        "age": 22,
        "grade": "B",
    }
    response = client.put("/student/1", json=student_data)
    assert response.status_code == 200
    updated_student = response.json()
    assert updated_student["name"] == student_data["name"]
    assert updated_student["age"] == student_data["age"]
    assert updated_student["grade"] == student_data["grade"]


def test_update_nonexistent_student():
    # Assuming there is no student with id=999 in the database
    student_data = {
        "name": "Jane Smith",
        "age": 22,
        "grade": "B",
    }
    response = client.put("/student/999", json=student_data)
    assert response.status_code == 404
    error = response.json()
    assert error["detail"] == "Student not found"


def test_delete_student():
    # Assuming there is a student with id=1 in the database
    response = client.delete("/student/1")
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert result["message"] == "Student deleted successfully"


def test_delete_nonexistent_student():
    # Assuming there is no student with id=999 in the database
    response = client.delete("/student/999")
    assert response.status_code == 404
    error = response.json()
    assert error["detail"] == "Student not found"
