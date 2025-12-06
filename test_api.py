import requests
import json
import sys

url = "http://localhost:8000/generate-puzzle"
payload = {
    "words": ["HELLO", "WORLD", "PYTHON", "FASTAPI"],
    "size": 15,
    "complexity": 0
}
headers = {
    "Content-Type": "application/json"
}

with open("test_output.txt", "w") as f:
    try:
        response = requests.post(url, json=payload, headers=headers)
        f.write(f"Status Code: {response.status_code}\n")
        f.write(f"Response Body: {response.text}\n")
    except Exception as e:
        f.write(f"Request failed: {e}\n")
