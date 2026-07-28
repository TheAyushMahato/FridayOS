from openwakeword.model import Model


class WakeDetector:

    def __init__(self):

        print("Loading Wake Word Engine...")

        self.model = Model()

        print("Wake Word Engine Ready.")

    def detect(self, audio):

        prediction = self.model.predict(audio)

        return prediction