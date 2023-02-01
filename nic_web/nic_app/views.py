from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def hello(request):
#     return HttpResponse('hello')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def discussion(request):
    return render(request, 'discussion.html')

def purchase(request):
    return render(request, 'purchase.html')

def tutorial(request):
    return render(request, 'tutorial.html')