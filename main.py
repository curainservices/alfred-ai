import os

print("🤖 ALFRED AI Starting...")

def fake_claude_response(user_input):
    return f"[Simulated Claude Response] I understand: {user_input}"

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("ALFRED: Goodbye!")
        break

    response = fake_claude_response(user_input)
    print("ALFRED:", response)
