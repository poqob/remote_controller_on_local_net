# define a class that resolves the packages
# then sends them to related computer input services


# packages:

# service: [keyboard(k)-mouse(m)-other(o)]


# service:'k'
# hotkey?: false
# input:'keys'(keyboard)


# may i convert it to a drag service :D
# service:'m'
# x:'numeric value'
# y:'numeric value'
from keyboard_service import KeyboardService
from model import Services, Model


class PackageHandler:
    def __new__(cls):
        raise TypeError("Static classes can't be instantied")

    @staticmethod
    def handle(data, serder_address) -> None:
        model = data.decode("utf-8")
        model = Model.fromJson(model)

        match model._service:
            case Services.KEYBOARD:
                print("keyboard input")
                KeyboardService.singlePressAndRelease(model._key)
            case Services.MOUSE:
                print("mouse input")
            case Services.OTHER:
                print("other input")
            case _:
                print("undefine input")
