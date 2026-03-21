from typing import Callable


def handle_voice_call(ai_handler: Callable[[str], str]):
    print("Voice call session started. Type your query (or 'quit' to exit).\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "bye"):
            print("Bank: Thank you for using Muryar Banki. Goodbye!")
            break

        response = ai_handler(user_input)
        print(f"Bank: {response}\n")
