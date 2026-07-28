from datetime import datetime
from utils.speak import speak


def handle_system_command(user):
    user = user.lower()

    # Current Time
    if "what time is it" in user or user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        return True

    # Today's Date
    if "what is today's date" in user or "today's date" in user:
        current_date = datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {current_date}.")
        return True

    # Today's Day
    if "what day is today" in user or user == "day":
        current_day = datetime.now().strftime("%A")
        speak(f"Today is {current_day}.")
        return True

    return False