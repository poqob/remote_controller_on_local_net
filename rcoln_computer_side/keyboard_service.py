import keyboard
from pipeline import *
import time
import threading

# {KeyboardService}
# keyable input types for keyboard service:

# [regular input]
# single character
# multiple character -> parse them into single character

# [special input]
# hotkey


# {Pipeline}
# i'll use queue data structure.
# keyboard service will accept requests and directs into a queue.
# the service is listening the queue and state changes. then takes action according to the queue.
# firstly i need a queue to receive requests(Model clss) and collect them.
# then i have to listen this queue watch the changes.
# make decision of press() or press_and_release() according to the pipeline's state.

# [click behaviour]
# tap modes: press and release[hotkey, single-multiple character], press(held)[single character]
# the pipeline will indicate the tap mode.


class KeyboardService:
    # fields
    # Create an event object to signal the thread to stop
    global stop_event
    global thread

    stop_event = threading.Event()

    def __new__(cls):
        raise TypeError("Static classes can't be instantied")

    # pop() method returns status, model.
    # up to status send model to press modes.
    global keyboardPipeline
    keyboardPipeline = Pipeline()

    # OPEN A THREAD
    @staticmethod
    def listen():
        while (
            not stop_event.is_set()
        ):  # Check if the event is set  # keyboardPipeline.pipelineStatus is PipelineStatuses.full:
            time.sleep(0.02)
            keystatus, model = keyboardPipeline.popEvent()
            match keystatus:
                case KeyStatuses.TAP_AND_RELEASE:
                    KeyboardService.singlePressAndRelease(model._key)
                case KeyStatuses.HELD:
                    KeyboardService.singlePress(model._key)

    @staticmethod
    def addEventToPipeline(event):
        keyboardPipeline.addEvent(event=event)

    @staticmethod
    def hotkey(hotkey):
        # keyboard.press_and_release("windows+d")
        KeyboardService.singlePressAndRelease(hotkey)

    # makes single character press (HELD)
    @staticmethod
    def singlePress(key):
        time.sleep(0.02)
        keyboard.press(key)

    # makes single character press and release (PAR, press and release)
    @staticmethod
    def singlePressAndRelease(key):
        keyboard.press_and_release(key)

    @staticmethod
    def stopService():
        stop_event.set()  # Set the event to stop the thread
        # thread.join()  # Wait for the thread to finish

    @staticmethod
    def startService():
        stop_event.clear()
        thread = threading.Thread(target=KeyboardService.listen)
        thread.start()
