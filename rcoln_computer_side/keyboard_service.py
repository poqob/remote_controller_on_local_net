import keyboard


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
    def __new__(cls):
        raise TypeError("Static classes can't be instantied")

    @staticmethod
    def hotkey(hotkey):
        # keyboard.press_and_release("windows+d")
        KeyboardService.singlePressAndRelease(hotkey)

    # makes single character press (HELD)
    @staticmethod
    def singlePress(key):
        keyboard.press(key)

    # makes key release up to given key
    @staticmethod
    def releaseKey(key):
        keyboard.release(key)

    # makes single character press and release (PAR, press and release)
    @staticmethod
    def singlePressAndRelease(key):
        keyboard.press_and_release(key)
