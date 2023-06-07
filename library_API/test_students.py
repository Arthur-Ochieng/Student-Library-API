from fastapi.testclient import TestClient

from .main import app
client = TestClient(app)


def test_get_student():
    response = client.get("/student/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "first_name": "Zach",
        "last_name": "Helsing",
        "date_of_birth": "1925-05-29",
        "email": "zinadine@gmail.com",
    }

def test_get_student_again():
    response = client.get("/student/1")
    assert response.status_code == 200
    student = response.json()
    assert "id" in student
    assert "first_name" in student
    assert "last_name" in student
    assert "date_of_birth" in student
    assert "email" in student


def test_get_students():
    response = client.get("/student/students")
    assert response.status_code == 200
    student = response.json()
    assert isinstance(student, list)
