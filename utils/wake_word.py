def wait_for_wake_word():

    while True:

        wake = input("\n🎤 Wake Word: ").strip().lower()

        if wake in [
            "friday",
            "hey friday",
            "hello friday"
        ]:
            return True