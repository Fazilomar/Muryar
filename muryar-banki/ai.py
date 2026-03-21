def detect_intent(text):
    text = text.lower()

    if "balance" in text:
        return "check_balance"

    elif "send" in text or "transfer" in text:
        return "transfer_money"

    elif "exit" in text:
        return "exit"

    return "unknown"
