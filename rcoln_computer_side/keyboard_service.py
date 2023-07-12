import keyboard


# i'll use queue data structure.
# keyboard service will accept requests and directs into a queue.
# the service is listening the queue and state changes. then takes action according to the queue.
# firstly i need a queue to receive requests(Model clss) and collect them.
# then i have to listen this queue watch the changes.


class KeyboardService:
    def __new__(cls):
        raise TypeError("Static classes can't be instantied")

    @staticmethod
    def press(key):
        keyboard.press(key)

    @staticmethod
    def hotkey():
        keyboard.press_and_release("windows+d")
