from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', hello, name='hello'),
    path('html', home, name='home'),
    
]
