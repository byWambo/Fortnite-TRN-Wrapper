from .item import Item


class Store:

    def __init__(self, data):
        self.items = [Item(item) for item in data]
