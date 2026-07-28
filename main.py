from router import process_command
from utils.whisper_voice import listen
from utils.speak import speak

print("===================================")
print("      🤖 Friday AI Assistant")
print("===================================")
print("Type 'voice' to talk.")
print("Type 'exit' to quit.\n")

speak("Hello Ayush. Friday is online.")

while True:

    try:

        user = input("You: ").strip()

        # Exit
        if user.lower() == "exit":
            process_command(user)
            break

        # Voice Mode
        if user.lower() == "voice":

            speak("Listening.")

            user = listen()

            if not user:
                speak("I didn't hear anything.")
                continue

        if not user:
            continue

        process_command(user)

    except KeyboardInterrupt:

        print("\n")

        speak("Shutting down.")

        break

    except Exception as e:

        print(f"\nError: {e}")

        speak("Something went wrong.")