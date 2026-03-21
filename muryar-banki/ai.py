def get_ai_response(user_input: str) -> str:
    user_input = user_input.strip().lower()

    if "balance" in user_input:
        return "Your current account balance is 50,000 Naira."
    elif "transfer" in user_input:
        return "Please provide the recipient account number and amount to transfer."
    elif "loan" in user_input:
        return "You are eligible for a loan of up to 200,000 Naira. Would you like to apply?"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! Welcome to Muryar Banki. How can I assist you today?"
    else:
        return "I'm sorry, I didn't understand that. Please try asking about your balance, transfers, or loans."
