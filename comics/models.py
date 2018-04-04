from django.db import models

# Create your models here.
class Comic(models.Model):
    title = models.CharField(max_length=100)
    issue = models.CharField(max_length=20)
    graded = models.CharField(max_length=200)
    key = models.CharField(max_length=500)

    def __str__(self):
        return self.title + " " +self.issue
