import requests


# create a API layer class to work with our endpoint
# to be able to send requests and get responses
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    # method GET to call the /api/hello endpoint and return the response as JSON
    def get_hello(self):
        response = requests.get(f"{self.base_url}/api/hello")
        return response.json()

    # method GET to call the /api/data_type endpoint
    # with parameter "value" and return the response as JSON
    # we will use it in test tests/api/test_data_type_api.py
    def get_data(self, value):
        response = requests.get(
            f"{self.base_url}/api/data_type", params={"value": value}
        )
        return response.json()
