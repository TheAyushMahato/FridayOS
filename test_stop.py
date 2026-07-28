from utils.speak import speak, stop_speaking
import time

speak("Hello Ayush. I am speaking for a long time so you can test stopping me.")

time.sleep(2)

stop_speaking()

print("Stopped!")