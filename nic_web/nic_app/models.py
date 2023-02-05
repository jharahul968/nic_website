from django.db import models

# Create your models here.

default_image = 'images/default.jpg'


class Project(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='images/projects/', default=default_image)

    def __str__(self):
        return self.name

class Ongoing(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/ongoing/', default=default_image)

    def __str__(self):
        return self.name

