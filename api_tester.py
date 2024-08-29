import requests
import json


class APITester:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def get_request(self, params=None):
        """Sends a GET request to the specified URL with parameters and returns a response in JSON format."""
        try:
            response = requests.get(self.base_url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    def set_headers(self, headers):
        """Sets additional headers."""
        self.headers.update(headers)


# Usage example
if __name__ == "__main__":
    # use base URL to get data
    api_tester = APITester("https://.......")

    # Set additional headers if necessary
    additional_headers = {'Authorization': 'Bearer YOUR_TOKEN'}
    api_tester.set_headers(additional_headers)

    # Example GET request
    response = api_tester.get_request()

    # Beautiful display of GET response
    if response:
        print("GET response (formatted):")
        print(json.dumps(response, indent=4, ensure_ascii=False))
    else:
        print("GET response: No data received or an error occurred.")
