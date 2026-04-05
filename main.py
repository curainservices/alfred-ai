print("🤖 ALFRED AI Starting...")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("ALFRED: Goodbye!")
        break

    print("ALFRED: I'm still learning, but I understand you said:", user_input)
