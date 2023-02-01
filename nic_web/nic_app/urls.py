from django.urls import path, include
from .views import *

urlpatterns = [
    # path('hello', hello, name='hello'),
    
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('discussion', discussion, name='discussion'),
    path('purchase', purchase, name='purchase'),
    path('tutorial', tutorial, name='tutorial')
    
]
