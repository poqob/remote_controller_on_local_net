import keyboard
from pipeline import Pipeline, KeyStatuses
import time
import multiprocessing


class KeyboardService:
    def __init__(self):
        self.keyboardPipeline = Pipeline()

    def listen(self):
        while True:
            keystatus, model = self.keyboardPipeline.popEvent()

            # controll the model if it is hotkey or not

            match keystatus:
                case KeyStatuses.TAP_AND_RELEASE:
                    self.singlePressAndRelease(model._key)
                case KeyStatuses.HELD:
                    self.singlePress(model._key)

    def addEventToPipeline(self, event):
        self.keyboardPipeline.addEvent(event=event)

    @staticmethod
    def singlePress(key):
        time.sleep(0.02)
        keyboard.press(key)

    @staticmethod
    def singlePressAndRelease(key):
        keyboard.press_and_release(key)


if __name__ == "__main__":
    ks = KeyboardService()

    process = multiprocessing.Process(target=ks.listen)
    process.start()

    # Stop the keyboard service by terminating the process
    process.terminate()
    process.join()
    print("ks stopped")
