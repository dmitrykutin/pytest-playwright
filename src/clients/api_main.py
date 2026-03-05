import requests


class APIClient:
    def __init__(self, base_url):
        """
        Initialize the API client.

        Args:
            base_url (str): The root URL of the API.

        Attributes:
            logs (list): Stores all requests and responses for debugging.
        """
        self.base_url = base_url
        self.logs = []  # List to keep track of all API requests and responses

    def request(self, method, endpoint, **kwargs):
        """
        Universal request method that handles all HTTP methods (GET, POST, etc.).
        Logs request and response details. Captures exceptions as well.

        Args:
            method (str): HTTP method ("GET", "POST", "PUT", etc.)
            endpoint (str): API endpoint, appended to the base URL
            **kwargs: Optional arguments for requests.request, e.g., params, json, headers

        Returns:
            requests.Response: The raw response object

        Raises:
            Exception: Any exception from requests.request is propagated after logging
        """
        url = f"{self.base_url}{endpoint}"  # Construct the full URL

        try:
            # Send the HTTP request using the requests library
            response = requests.request(method, url, **kwargs)

            # Log the request and response details
            # This includes method, URL, query parameters, JSON payload, status code, and response text
            self.logs.append(
                f"{method} {url} "
                f"params={kwargs.get('params')} "
                f"json={kwargs.get('json')} "
                f"-> {response.status_code} "
                f"{response.text}"
            )

            # Raise HTTPError for bad HTTP responses (4xx or 5xx)
            response.raise_for_status()

            # Return the full response object for further processing if needed
            return response

        except Exception as e:
            # If any exception occurs (network, HTTP error, etc.), log it with details
            self.logs.append(f"{method} {url} FAILED: {e}")
            # Re-raise the exception so that tests or calling code can handle it
            raise

    def get_hello(self):
        """
        Sends a GET request to '/api/hello' endpoint.

        Returns:
            dict: The JSON response parsed into a Python dictionary
        """
        return self.request("GET", "/api/hello").json()

    def get_data(self, value):
        """
        Sends a GET request to '/api/data_type' endpoint with a query parameter.

        Args:
            value: The value to be sent as query parameter 'value'

        Returns:
            dict: The JSON response parsed into a Python dictionary
        """
        return self.request(
            "GET",
            "/api/data_type",
            params={"value": value},  # Query parameters for GET request
        ).json()

    def create_user(self, first_name, last_name):
        """
        Sends a POST request to '/users' endpoint to create a new user.

        Args:
            first_name (str): First name of the user
            last_name (str): Last name of the user

        Returns:
            dict: The JSON response parsed into a Python dictionary
        """
        payload = {"first_name": first_name, "last_name": last_name}  # JSON body
        return self.request("POST", "/users", json=payload).json()

    def get_users(self):
        """
        Sends a GET request to '/users' endpoint to retrieve all users.

        Returns:
            list: The JSON response parsed into a Python list
        """
        return self.request("GET", "/users").json()
