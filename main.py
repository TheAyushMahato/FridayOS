from ai import ask_ai
from brain import load_memory

from commands.memory import handle_memory_command
from commands.apps import handle_app_command
from commands.web import handle_web_command
from commands.system import handle_system_command

from utils.voice import listen

memory = load_memory()

print("🤖 Friday AI Assistant Started!")
print("Type your message or type 'voice' to use the microphone.")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ").strip()

    # Voice Mode
    if user.lower() == "voice":
        user = listen()

        if not user:
            continue

    # Handle memory commands
    if handle_memory_command(user, memory):
        memory = load_memory()
        continue

    # Handle app commands
    if handle_app_command(user):
        continue

    # Handle web commands
    if handle_web_command(user):
        continue

    # Handle system commands
    if handle_system_command(user):
        continue

    # Exit
    if user.lower() == "exit":
        print("Friday: Goodbye!")
        break

    # AI Chat
    reply = ask_ai(user)
    print(f"\nFriday: {reply}")