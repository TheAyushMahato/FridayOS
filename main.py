from ai import ask_ai
from brain import load_memory
from commands.memory import handle_memory_command
from commands.apps import handle_app_command
from commands.web import handle_web_command
from commands.system import handle_system_command

memory = load_memory()

while True:
    user = input("You: ")

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
        break

    # AI Chat
    reply = ask_ai(user)
    print("\nFriday:", reply)