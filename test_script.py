import requests

url = "https://airbills-python-backend.onrender.com"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
