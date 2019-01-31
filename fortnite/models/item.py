from ..utils.raritys import Rarity
from ..utils.stores import Category


class Item:

    def __init__(self, data):
        self.image = data['imageUrl']
        self.manifest = data['manifestId']
        self.name = data['name']
        self.rarity = Rarity(data['rarity'])
        self.category = Category(data['storeCategory'])
        self.price = data['vBucks']
