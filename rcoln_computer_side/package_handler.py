from model import Model
from servicesEnum import Services


# solve packages to models then return package service type and package's model
class PackageHandler:
    # fields

    # new
    def __new__(cls):
        raise TypeError("Static classes can't be instantied")

    @staticmethod
    def handle(data, sender_address):
        model = data.decode("utf-8")
        model = Model.fromJson(model)
        service = None
        match model.service:
            case Services.KEYBOARD.value:
                print("keyboard input")
                service = Services.KEYBOARD
                # ServiceHandler.keyboard(model=model)
            case Services.MOUSE.value:
                print("mouse input")
                service = Services.MOUSE
            case Services.OTHER.value:
                print("other input")
                service = Services.OTHER
            case _:
                print(f"undefine input: {model.service}")
                service = Services.OTHER
        return service, model
