import pytest


@pytest.mark.api
def test_get_users(api_client):
    # request the GET method from api_main.py get_users and save the response in variable "response"
    # response is a JSON with "message" and "data" where "data" contains a list of users
    response = api_client.get_users()
    # here check the response json
    assert response["message"] == "Users retrieved"
    assert isinstance(response["data"], list)
