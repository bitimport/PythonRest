import requests

# Replace with the actual URL where the API is hosted
API_URL = "http://127.0.0.1:5000/greet?name=John"

def consume_api():
    try:
        # Example GET request
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Status Code: {response.status_code}")

        # Process the response
        data = response.json()
        print("Response from API:", data)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    consume_api()