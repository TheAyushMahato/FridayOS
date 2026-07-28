from ai import ask_ai, clear_history
from brain import load_memory

from commands.memory import handle_memory_command
from commands.apps import handle_app_command
from commands.web import handle_web_command
from commands.system import handle_system_command

from utils.speak import speak


memory = load_memory()


def process_command(user):
    global memory

    if not user:
        return

    user = user.strip()

    # Exit
    if user.lower() == "exit":
        speak("Goodbye Ayush.")
        clear_history()
        return "exit"

    # Clear Conversation
    if user.lower() in [
        "clear chat",
        "clear history",
        "reset chat",
        "new chat"
    ]:
        clear_history()
        speak("Conversation cleared.")
        return

    # Memory
    if handle_memory_command(user, memory):
        memory = load_memory()
        return

    # Apps
    if handle_app_command(user):
        return

    # Web
    if handle_web_command(user):
        return

    # System
    if handle_system_command(user):
        return

    # AI
    reply = ask_ai(user)

    if reply:
        speak(reply)
    else:
        speak("Sorry, I couldn't get a response.")