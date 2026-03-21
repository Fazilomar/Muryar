import os
import requests


def make_call(phone: str) -> dict:
    api_key = os.environ.get("AT_API_KEY", "")
    username = os.environ.get("AT_USERNAME", "sandbox")
    caller_id = os.environ.get("AT_CALLER_ID", "")
    base_url = os.environ.get("BASE_URL", "")

    url = "https://voice.africastalking.com/call"

    payload = {
        "username": username,
        "to": phone,
        "from": caller_id,
        "callbackUrl": f"{base_url}/voice",
    }

    headers = {
        "apiKey": api_key,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
