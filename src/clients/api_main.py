import requests


# create a API class to work with our endpoint
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    # method GET to call the /api/hello endpoint and return the response as JSON
    def get_hello(self):
        response = requests.get(f"{self.base_url}/api/hello")
        return response.json()
