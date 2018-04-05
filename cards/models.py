from django.db import models
import requests
import time

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    set = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def findUrl(self):
        payload = {'q':self.name,'order':self.set}
        r = requests.get('https://api.scryfall.com/cards/search', params=payload)
        time.sleep(0.1)
        return r.json()['data'][0]['image_uris']['small']

    def price(self):
        payload = {'q':self.name,'order':self.set}
        r = requests.get('https://api.scryfall.com/cards/search', params=payload)
        time.sleep(0.1)
        return r.json()['data'][0]['usd']
