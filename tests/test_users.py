import requests


BASE_URL = "http://127.0.0.1:8000/users/"


def test_users_invalid_password():
    """
    Test calling the users endpoint with an invalid password.
    Expected result: HTTP 200 with empty response.
    """
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200


def test_users_valid_password():
    """
    Test calling the users endpoint with a valid password.
    Expected result: HTTP 401 with empty response.
    """
    params = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 401
