from enum import Enum
from types import SimpleNamespace
import json


class Services(Enum):
    KEYBOARD = (0,)
    MOUSE = (1,)
    OTHER = (2,)


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
