import queue
from enum import Enum
from model import Model


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

        if next_event.key == popped._key:
            self.status = KeyStatuses.HELD
        else:
            self.status = KeyStatuses.TAP_AND_RELEASE
        # print("zortt from pipeline pop()")
        # print(f"status: {self.status.name}, key: {popped._key}")
        return self.status, popped
