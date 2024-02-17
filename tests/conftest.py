import os

from fastapi.testclient import TestClient
import pytest
from main import app


@pytest.fixture(scope="function")
def client() -> GeneratorExit:
    with TestClient(app) as c:
        yield c
