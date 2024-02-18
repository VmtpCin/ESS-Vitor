from fastapi.testclient import TestClient
from pytest_bdd import given, when, then, scenarios
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


@pytest.fixture()
def user_mock():
    username = "Hortifruti"
    email = username + "@gmail.com"
    cnpj = "1234567890"
    password = "1234"
    categoria = "Textil"

    store = Store(username=username, cnpj=cnpj, email=email, categoria=categoria, password=password)

    usuario = {"cnpj": store.cnpj,
               "password": store.password,
                "username": store.username,
                "email": store.email,
                "categoria": store.categoria}

    return usuario


def test_signup_screen(user_mock):
    user_mock["categoria"] = user_mock["categoria"].__dict__
    response = client.post("/signup/", json=user_mock)
    assert response.status_code == 200

# @when("I write <store_name> in the 'store name' field")
# def when_write_store_name(store_name):
#     # Use your testing framework to simulate writing in the field
#     pass
#
# @when("I write <password> in the 'password' field")
# def when_write_password(password):
#     # Use your testing framework to simulate writing in the field
#     pass
#
# @when("I write <email> in the 'email' field")
# def when_write_email(email):
#     # Use your testing framework to simulate writing in the field
#     pass
#
# @then("I see the message <message>")
# def then_see_message(message):
#     # Use your testing framework to check if the expected message is displayed
#     pass

