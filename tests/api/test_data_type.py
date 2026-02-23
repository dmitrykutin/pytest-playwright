import pytest


# this is api test with parameterization
# three different values and expected results for them
# and then it asserts that the response from the API is the same as expected
@pytest.mark.parametrize(
    "value, expected", [(10, "integer"), (10.1, "float"), ("text", "string")]
)
@pytest.mark.api
def test_data_type_api(api_client, value, expected):
    response = api_client.get_data(value)
    assert response == {"data_type": expected}
