from ai import get_ai_response
from voice_call import handle_voice_call


def main():
    print("Muryar Banki - AI Voice Banking Assistant")
    print("==========================================")
    handle_voice_call(get_ai_response)


if __name__ == "__main__":
    main()
