import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_equipment(client):
    response = client.get("/api/equipment")

    assert response.status_code == 200
    assert response.get_json() == [
        {
            "id": 101,
            "name": "Flight Control unit",
            "type": "FCU",
            "status": "operational"
        },
        {
            "id": 102,
            "name": "Flight Control system",
            "type": "FCU",
            "status": "operational"
        }
    ]


def test_get_equipment_by_id(client):
    response = client.get("/api/equipment/101")

    assert response.status_code == 200
    assert response.get_json() == {
        "id": 101,
        "name": "Flight Control unit",
        "type": "FCU",
        "status": "operational"
    }


def test_get_equipment_by_id_not_found(client):
    response = client.get("/api/equipment/999")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Equipment not found"}