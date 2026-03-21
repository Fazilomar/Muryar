import africastalking
import os

username = "sandbox"
api_key = os.environ.get("AT_API_KEY")

africastalking.initialize(username, api_key)

voice = africastalking.Voice


def make_call(phone):
    try:
        response = voice.call(
            callFrom="+254711XXXYYY",
            callTo=[phone]
        )
        return {"status": "calling", "response": str(response)}

    except Exception as e:
        return {"error": str(e)}
