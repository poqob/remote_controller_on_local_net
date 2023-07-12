# define a class that resolves the packages
# then sends them to related computer input services


# packages:

# service: [keyboard(k)-mouse(m)-other(o)]


# service:'k'
# key:'key'(keyboard)


# may i convert it to a drag service :D
# service:'m'
# x:'numeric value'
# y:'numeric value'
import json
from types import SimpleNamespace
from keyboard_service import KeyboardService


class Model:
    _service = None
    _key = None

    def __init__(self, service, key) -> None:
        self._service = service
        self._key = key

    def toJson(self) -> str:
        return json.dumps(self.__dict__)

    def fromJson(inpt):
        # Parse JSON into an object with attributes corresponding to dict keys.
        x = json.loads(inpt, object_hook=lambda d: SimpleNamespace(**d))
        # print(x._service, x._key)
        return x


class PackageHandler:
    def __new__(cls):
        raise TypeError("Static classes can't be instantied")

    @staticmethod
    def handle(data, serder_address) -> None:
        model = data.decode("utf-8")
        model = Model.fromJson(model)

        match model._service:
            case "k":
                print("keyboard input")
                KeyboardService.hotkey()
            case "m":
                print("mouse input")
            case _:
                print("other input :s")
