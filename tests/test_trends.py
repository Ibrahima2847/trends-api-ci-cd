import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_trends():
    response = client.get("/trends")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
