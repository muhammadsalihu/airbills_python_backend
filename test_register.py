import requests

BASE_URL = "http://127.0.0.1:8000"  # Update if running on a different host/port

def test_register():
    url = f"{BASE_URL}/auth/register"
    payload = {
        "email": "testuser@example.com",
        "password": "securepassword123"
    }
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response:", response.json())

if __name__ == "__main__":
    test_register()
