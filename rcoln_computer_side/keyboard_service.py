import keyboard
from pipeline import Pipeline, KeyStatuses
import time


class KeyboardService:
    def __init__(self):
        self.keyboardPipeline = Pipeline()

    def listen(self):
        while True:
            time.sleep(0.02)
            keystatus, model = self.keyboardPipeline.popEvent()

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
