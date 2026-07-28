import speech_recognition as sr


recognizer = sr.Recognizer()

# Better defaults
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5


def listen():
    """
    Listen to the microphone and return recognized text.
    Returns "" if nothing useful was heard.
    """

    try:
        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            # Reduce background noise
            recognizer.adjust_for_ambient_noise(source, duration=1)

            # Wait up to 5 seconds for speech.
            # Record for a maximum of 8 seconds.
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("🧠 Recognizing...")

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        text = text.strip().lower()

        print(f"You said: {text}")

        return text

    except sr.WaitTimeoutError:
        print("Friday: I didn't hear anything.")
        return ""

    except sr.UnknownValueError:
        print("Friday: Sorry, I couldn't understand you.")
        return ""

    except sr.RequestError:
        print("Friday: Speech recognition service is unavailable.")
        return ""

    except KeyboardInterrupt:
        return ""

    except Exception as e:
        print(f"Voice Error: {e}")
        return ""