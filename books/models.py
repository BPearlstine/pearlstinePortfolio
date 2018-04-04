from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=300)
    genre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50)

    def __str__(self):
        return self.title
