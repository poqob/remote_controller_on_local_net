from servicesEnum import Services
from model import Model
import time
import keyboard
import threading
from enum import Enum
import queue


class KeyStatuses(Enum):
    TAP_AND_RELEASE = 0
    HELD = 1


class PipelineStatuses(Enum):
    empty = 0
    full = 1


class Pipeline:
    pipelineStatus = PipelineStatuses.empty
    status = None
    q1 = queue.Queue()

    def __init__(self) -> None:
        pass

    def addEvent(self, event):
        self.q1.put(event)
        self.pipelineStatus = PipelineStatuses.full

    def popEvent(self):
        popped = self.q1.get()
        if self.q1.qsize() >= 1:
            next_event = self.q1.queue[0]
        else:
            next_event = Model(0, "")
            self.pipelineStatus = PipelineStatuses.empty

        if next_event._key == popped._key:
            self.status = KeyStatuses.HELD
        else:
            self.status = KeyStatuses.TAP_AND_RELEASE
        print("zortt from pipeline pop()")
        print(f"status: {self.status.name}, key: {popped._key}")
        return self.status, popped


class ServiceHandler:
    def __init__(self) -> None:
        self.keyboardService = None

    def accept(self, service, model):
        if service == Services.KEYBOARD:
            self._keyboard(model=model)
        else:
            print(service)

    def _keyboard(self, model) -> None:
        if self.keyboardService is None:
            self.keyboardService = KeyboardService()
            self.keyboardService.startService()
        self.keyboardService.addEventToPipeline(model)

    def stopServices(self):
        if self.keyboardService:
            self.keyboardService.stopService()
            self.keyboardService = None


if __name__ == "__main__":
    sh = ServiceHandler()
    model = Model(0, "windows+d")
    sh.accept(Services.KEYBOARD, model)
    time.sleep(1)
    sh.killServices()


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
