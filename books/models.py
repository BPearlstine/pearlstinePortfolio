from django.db import models
import requests
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=300)
    genre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=50)

    def cover(self):
            payload = {'q':self.isbn,}
            r = requests.get('https://www.googleapis.com/books/v1/volumes', params=payload)
            if r.status_code == 200:
                 return r.json()['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']
            else:
                 return "# "

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
