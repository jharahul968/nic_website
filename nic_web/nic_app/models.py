from django.db import models
from django.contrib.auth.models import User

# Create your models here.

default_image = 'images/default.jpg'


class Project(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/projects/', default=default_image)
    added_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    items = models.ManyToManyField(Project, through='CartItem')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}\'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Project, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user}\'s {self.item} - {self.quantity}"