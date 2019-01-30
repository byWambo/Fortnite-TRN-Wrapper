from . import api


class Client:

    def __init__(self, key):
        self.key = key
        self.api = api.API(self.key)
