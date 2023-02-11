from django.urls import path, include
from .views import *

app_name='nic_app'

urlpatterns = [
    # path('hello', hello, name='hello'),
    
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('discussion', discussion, name='discussion'),
    path('projects', projects, name='projects'),
    path('tutorial', tutorial, name='tutorial'),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
    path("password_reset", password_reset_request, name="password_reset"),
    path("change_username", change_username, name="change_username"),
    path('user',user,name='user'),
    path('cart',cart,name='cart'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>', remove_from_cart, name='remove_from_cart'),
    path('item/<int:pk>', item, name='item'),
    path('buy/<int:pk>', buy, name='buy'),
]
