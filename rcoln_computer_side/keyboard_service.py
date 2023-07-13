import keyboard
from pipeline import Pipeline, KeyStatuses
import time
import threading


class KeyboardService:
    def __init__(self):
        self.keyboardPipeline = Pipeline()
        self.startService()
        self.flag = threading.Event()

    def startService(self):
        self.thread = threading.Thread(target=self.listen)
        self.thread.daemon = True
        self.flag = False
        self.thread.start()

    def stopService(self):
        self.flag = True
        self.thread.join()

    def listen(self):
        while self.flag == False:
            time.sleep(0.02)
            keystatus, model = self.keyboardPipeline.popEvent()

            if keystatus == KeyStatuses.TAP_AND_RELEASE:
                self.singlePressAndRelease(model._key)
            elif keystatus == KeyStatuses.HELD:
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
