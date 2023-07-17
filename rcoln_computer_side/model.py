from types import SimpleNamespace
import json


class Model:
    service = None
    key = None
    behaviour = None

    def __init__(self, service, key, behaviour) -> None:
        self.service = service
        self.key = key
        self.behaviour = behaviour

    def toJson(self) -> str:
        return json.dumps(self.__dict__)

    def fromJson(inpt):
        # Parse JSON into an object with attributes corresponding to dict keys.
        x = json.loads(inpt, object_hook=lambda d: SimpleNamespace(**d))
        # print(x._service, x._key)
        return x
