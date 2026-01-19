from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_price():
    response = client.get("/api/prices/AAPL")
    assert response.status_code == 200


def test_get_prediction():
    response = client.get("/api/predictions/AAPL")
    assert response.status_code == 200
    assert response.json()["ticker"] == "AAPL"
