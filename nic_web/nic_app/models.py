from django.db import models

# Create your models here.

default_image = 'images/default.jpg'


class Instrument(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default=default_image)

    def __str__(self):
        return self.name
