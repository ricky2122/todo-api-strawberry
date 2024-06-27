import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(name="client")
def client_fixture():
    client = TestClient(app)
    yield client
