import africastalking

username = "sandbox"
api_key = "YOUR_API_KEY"   # 🔴 Replace this

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
