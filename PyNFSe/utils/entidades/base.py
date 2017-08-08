import json

class Entidade(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
