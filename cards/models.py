from django.db import models
from ratelimit import rate_limited
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

    @rate_limited(0.1)
    def findUrl(self):
        payload = {'q':self.name,'order':self.set}
        r = requests.get('https://api.scryfall.com/cards/search', params=payload)

        return r.json()['data'][0]['image_uris']['small']

    @rate_limited(0.1)
    def price(self):
        payload = {'q':self.name,'order':self.set}
        r = requests.get('https://api.scryfall.com/cards/search', params=payload)

        return r.json()['data'][0]['usd']

    class Meta:
        ordering = ['-id']
