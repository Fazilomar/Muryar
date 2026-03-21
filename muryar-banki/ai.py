def detect_intent(text: str) -> str:
    text = text.strip().lower()

    if "balance" in text:
        return "check_balance"
    elif "transfer" in text:
        return "transfer_funds"
    elif "loan" in text:
        return "request_loan"
    elif "hello" in text or "hi" in text:
        return "greeting"
    else:
        return "unknown"
