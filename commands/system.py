from datetime import datetime


def handle_system_command(user):
    user = user.lower()

    if "what time is it" in user or user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Friday: The current time is {current_time}.")
        return True

    return False