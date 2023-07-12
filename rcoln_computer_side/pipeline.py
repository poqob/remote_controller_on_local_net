#
import queue
from enum import Enum
from model import Model


class Statuses(Enum):
    TAP_AND_RELEASE = (0,)
    HELD = (1,)


class PipelineStatuses(Enum):
    empty = (0,)
    full = (1,)


class Pipeline:
    pipelineStatus = PipelineStatuses.empty
    status = None
    q1 = queue.Queue()

    # simulating keyboard service stream
    def __init__(self) -> None:
        self.addEvent(Model(0, "s"))
        self.addEvent(Model(0, "f"))
        self.addEvent(Model(0, "p"))
        self.addEvent(Model(0, "d"))
        self.addEvent(Model(0, "d"))
        self.addEvent(Model(0, "g"))

    # server_service_handler will add events
    def addEvent(self, event):
        self.q1.put(event)
        self.pipelineStatus = PipelineStatuses.full

    # keyboard service will pop events
    def pop(self):
        # controlling if popped queue item and next queue item value is equal each other.
        # checking if consecutive elements have equal values.
        popped = self.q1.get()
        if self.q1.qsize() >= 1:
            next = self.q1.queue[0]
        else:
            next = Model(0, "")
            self.pipelineStatus = PipelineStatuses.empty

        # setting status up to equality state of consecutive elements.
        if next._key is popped._key:
            self.status = Statuses.HELD
        else:
            self.status = Statuses.TAP_AND_RELEASE

        print(f"status: {self.status.name}, key: {popped._key}")
        return self.status, popped
        # print(f"{self.status.name} keycurr: {curr._key} keyprev: {prev._key}")
