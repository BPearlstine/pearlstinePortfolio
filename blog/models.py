from django.db import models
import logging

logger = logging.getLogger(pearlstinePortfolio.blog.models)
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        logger.info("Summary for blog: %s", self.body[:200])
        return self.body[:200]

    def pub_day(self):
        logger.info("pub_date for blog: %s", pub_date.strftime('%x'))
        return self.pub_date.strftime('%x')

    def __str__(self):
        logger.info("blog toString: %s", self.title)
        return self.title

    class Meta:
        ordering = ['-id']
