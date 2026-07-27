import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")

        return text

    except sr.UnknownValueError:
        print("Friday: Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        print("Friday: Speech service unavailable.")
        return ""