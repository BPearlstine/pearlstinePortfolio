from django.db import models
from ratelimit import rate_limited
import requests
import time
import logging

logger = logging.getLogger(__name__)
# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    set = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    # @rate_limited(0.1)
    # def findUrl(self):
    #     payload = {'q':self.name,'order':self.set}
    #     r = requests.get('https://api.scryfall.com/cards/search', params=payload)
    #     if r.status_code == 200:
    #         logger.info("card image uri: %s", r.json()['data'][0]['image_uris']['small'])
    #         return r.json()['data'][0]['image_uris']['small']
    #     else:
    #         return "#"

    # @rate_limited(0.1)
    # def price(self):
    #     payload = {'q':self.name,'order':self.set}
    #     r = requests.get('https://api.scryfall.com/cards/search', params=payload)
    #     if r.status_code == 200:
    #         try:
    #             return r.json()['data'][0]['usd']
    #         except:
    #             return "no current data"
    #     else:
    #         return "no data"

    class Meta:
        ordering = ['-id']
