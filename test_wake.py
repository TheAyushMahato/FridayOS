from utils.wake_word import wait_for_wake_word

print("🤖 Friday Wake Test")
print("Type 'Friday' to wake the assistant.\n")

while True:

    wait_for_wake_word()

    print("✅ Wake Word Detected!")
    print("Friday: Yes, Ayush.\n")