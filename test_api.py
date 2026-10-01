from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_home_planner():
    response = client.post(
        "/generate-home",
        json={
            "budget": 10000,
            "room_type": "Bedroom",
            "preferences": "Modern"
        }
    )

    assert response.status_code == 200


def test_party_planner():
    response = client.post(
        "/generate-party",
        json={
            "budget": 20000,
            "guests": 50,
            "event_type": "Birthday"
        }
    )

    assert response.status_code == 200
