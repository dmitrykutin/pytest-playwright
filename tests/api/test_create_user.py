import pytest
from tests.data.factories import user_factory


# It's a test for the API endpoint /users that creates a user in the database
# Here we use factory to generate random user data (look factories.py)
# and use it in parametrize to run the test with different data


@pytest.mark.parametrize("user", user_factory(2))
@pytest.mark.api
def test_create_user(api_client, user):
    # request the POST method from api_main.py create_user with generated user data
    # and save the response in variable "response"
    # response is a JSON with "message" and "data" where "data" contains the user info and id
    response = api_client.create_user(user["first_name"], user["last_name"])
    # here check the response json with data we sent
    assert response["message"] == "User created"
    assert response["data"]["first_name"] == user["first_name"]
    assert response["data"]["last_name"] == user["last_name"]
    assert "id" in response["data"]
