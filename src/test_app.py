from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_predict_valid_input():
    payload = {
        "features": [
            [5.1, 3.5, 1.4, 0.2]
        ]
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    result = response.json()
    print("Prediction:", result["prediction"])
    assert "prediction" in result
    assert isinstance(result["prediction"], list)
    assert len(result["prediction"]) == 1
