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
        print(json.dumps(self.__dict__))
        return json.dumps(self.__dict__)

    def fromJson(inpt):
        # Parse JSON into an object with attributes corresponding to dict keys.
        x = json.loads(inpt, object_hook=lambda d: SimpleNamespace(**d))
        # print(x._service, x._key)
        return x


class Handler:
    def __init__(self, ip, port, key, service) -> None:
        self.ip = ip
        self.port = port
        self.key = key
        self.service = service
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self):
        model = Model(service=self.service.value, key=self.key)
        # print(model.toJson())
        bytes_data = model.toJson().encode("utf-8")
        self.sock.sendto(bytes_data, (self.ip, self.port))


if __name__ == "__main__":
    ip = input("local-ip:")
    port = int(input("port:"))
    key = input("key:")
    service = Services.KEYBOARD
    handler = Handler(ip, port, key, service)
    handler.send()
