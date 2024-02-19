from fastapi.testclient import TestClient
from pytest_bdd import given, when, then, scenarios, parser
import pytest
import json
from Models.store import Categoria, Store
from main import app

client = TestClient(app)


STORE_DATA_FILE_TEST = "store_data_test.json"

def load_store_data():
    try:
        with open(STORE_DATA_FILE_TEST, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Helper function to save user data to JSON file
def save_store_data(data):
    with open(STORE_DATA_FILE_TEST, "w") as f:
        json.dump(data, f, indent=4)

def test_signup_screen():
    user_mock = {
        "u": "Hortifruti",
        "c": "1234567890",
        "e": "vitu@gmail.com",
        "cat": "Textil",
        "p": "1234"
    }
    response = client.post("/stores/signup")
    #print(response.json())
    assert response.status_code == 200


# @pytest.fixture()
# def user_mock():
#     username = "Hortifruti"
#     email = username + "@gmail.com"
#     cnpj = "1234567890"
#     password = "1234"
#     categoria = "Textil"
#
#     store = Store(username=username, cnpj=cnpj, email=email, categoria=categoria, password=password)
#
#     usuario = {"cnpj": store.cnpj,
#                "password": store.password,
#                 "username": store.username,
#                 "email": store.email,
#                 "categoria": store.categoria}
#
#     return usuario
