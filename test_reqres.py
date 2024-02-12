import requests
from jsonschema import validate
from schemas import post_register_user, post_create_user, put_update_user, post_login_user, get_list_users


def test_get_user_not_found():
    response = requests.get("https://reqres.in/api/unknown/23")
    assert response.status_code == 404


def test_post_create_user():
    response = requests.post("https://reqres.in/api/users", data={"name": "morpheus", "job": "leader"})
    assert response.status_code == 201
    validate(response.json(), schema=post_create_user)


def test_delete_users():
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204


def test_put_update_user():
    response = requests.put("https://reqres.in/api/users/2", data={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200
    validate(response.json(), schema=put_update_user)


def test_post_reg_successful():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    assert response.status_code == 200
    validate(response.json(), schema=post_register_user)


def test_post_reg_no_credentials():
    response = requests.post("https://reqres.in/api/register")
    assert response.status_code == 400
    assert response.json().get("error") == "Missing email or username"


def test_post_login_successful():
    response = requests.post("https://reqres.in/api/login",
                             data={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    assert response.status_code == 200
    validate(response.json(), schema=post_login_user)


def test_post_login_no_credentials():
    response = requests.post("https://reqres.in/api/login")
    assert response.status_code == 400
    assert response.json().get("error") == "Missing email or username"


def test_get_list_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    validate(response.json(), schema=get_list_users)


def test_login_no_password():
    response = requests.post("https://reqres.in/api/register", data={"email": "eve.holt@reqres.in"})
    assert response.status_code == 400
    assert response.json().get("error") == "Missing password"


def test_login_no_email():
    response = requests.post("https://reqres.in/api/register", data={"password": "cityslicka"})
    assert response.status_code == 400
    assert response.json().get("error") == "Missing email or username"
