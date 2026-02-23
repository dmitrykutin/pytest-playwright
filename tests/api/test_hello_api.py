# this is our one api test file for testing /api/hello endpoint


import pytest


@pytest.mark.api
def test_hello_api(api_client):
    # call the get_hello method of the API client,
    # which will call the /api/hello endpoint and return the response as JSON
    response = api_client.get_hello()
    # check if the response is equal to {"message": "hello"}
    assert response == {"message": "hello"}
