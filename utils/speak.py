import subprocess
import re

VOICE = "Tara"


def clean_text(text):
    # Extra spaces hatao
    text = re.sub(r"\s+", " ", text)

    # Markdown characters hatao
    text = text.replace("*", "")
    text = text.replace("#", "")
    text = text.replace("`", "")

    return text.strip()


def speak(text):
    text = clean_text(text)

    print(f"\nFriday: {text}")

    subprocess.run([
        "say",
        "-v",
        VOICE,
        text
    ])