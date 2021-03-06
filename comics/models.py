from django.db import models
import requests
import time
import logging

logger = logging.getLogger(__name__)
# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    graded = models.CharField(max_length=200)
    key = models.CharField(max_length=500)
    publisher = models.CharField(max_length=50,default='unknown')

    def __str__(self):
        return self.title + " " +self.issue

    class Meta:
        ordering = ['-id']
    # def cover(self):
    #
    #     vineKey = 2cffea4751659400ae5c38b31cbb63890d8c1e73
    #     payload = {'api_key':vineKey,'order':self.set}
    #     r = requests.get('http://comicvine.gamespot.com/api/issue', params=payload)
    #     time.sleep(0.1)
    #     return r.json()
