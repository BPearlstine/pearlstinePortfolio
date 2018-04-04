from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    set = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.name 
