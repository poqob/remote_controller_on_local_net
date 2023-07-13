import socket
from enum import Enum
from types import SimpleNamespace
import json


class Services(Enum):
    KEYBOARD = 0
    MOUSE = 1
    OTHER = 2


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


# 0: create socket, 1: socket type-UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Replace with the desired destination IP address
destination_address = "192.168.1.103"  # address of the computer server launch.
destination_port = 5100  # Replace with the port in config file.


def send():
    # serv = input("services: [k,m,o]; k:keyboard, m:mouse, o:other \nservice:")
    key = input("key:")
    model = Model(service=Services.KEYBOARD.value, key=key)
    print(model.toJson())
    bytes_data = model.toJson().encode("utf-8")
    sock.sendto(bytes_data, (destination_address, destination_port))


send()
