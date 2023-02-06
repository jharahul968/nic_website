from django.db import models
from django.contrib.auth.models import User

# Create your models here.

default_image = 'images/default.jpg'


class Project(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/projects/', default=default_image)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/cart/', default=default_image)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} - {self.item} ({self.quantity})"

