from .models.store import Store

import fortnite
import requests


class API:

    def __init__(self, key):
        self.header = {'TRN-Api-Key': key}

    def get_stats(self, name: str, platform=fortnite.Platforms.PC):
        url = 'https://api.fortnitetracker.com/v1/profile/pc/{}'.format(platform.name, name)
        respond = requests.get(url, headers=self.header)
        return respond.json()

    def get_match(self, account_id: int):
        url = 'https://api.fortnitetracker.com/v1/profile/account/}/matches '.format(account_id)
        respond = requests.get(url, headers=self.header)
        return respond.json()

    def get_store(self):
        url = 'https://api.fortnitetracker.com/v1/store'
        respond = requests.get(url, headers=self.header)
        return Store(respond.json())

    def get_challenges(self):
        url = 'https://api.fortnitetracker.com/v1/challenges '
        respond = requests.get(url, headers=self.header)
        return respond.json()
