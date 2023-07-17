from servicesEnum import Services
from model import Model
import time
import keyboard
import threading
import queue
from behaviour import Behaviour

# why i cannot seperate this module to modules????


class Pipeline:
    def __init__(self) -> None:
        self.q1 = queue.Queue()

    def addEvent(self, event):
        self.q1.put(event)

    def popEvent(self) -> Model:
        return self.q1.get()


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

    def listen(self):
        while self.flag == False:
            model = self.keyboardPipeline.popEvent()
            behaviour = model.behaviour
            if behaviour == Behaviour.PRESS_AND_RELEASE.value:
                self.singlePressAndRelease(model.key)
            elif behaviour == Behaviour.HOLD.value:
                self.held(model.key)

    def addEventToPipeline(self, event):
        self.keyboardPipeline.addEvent(event=event)

    @staticmethod
    def held(key):
        time.sleep(0.02)
        keyboard.press(key)

    @staticmethod
    def singlePressAndRelease(key):
        keyboard.press_and_release(key)


if __name__ == "__main__":
    sh = ServiceHandler()
    model = Model(0, "windows+d", 0)
    sh.accept(Services.KEYBOARD, model)
    time.sleep(1)
    sh.killServices()
