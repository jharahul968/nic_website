from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from django.db.models import F

# Create your views here.

# def hello(request):
#     return HttpResponse('hello')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("nic_app:home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("nic_app:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("nic_app:home")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'mail.ioehub@gmail.com',
                                  [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form": password_reset_form})


@login_required
def change_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        user = User.objects.get(username=request.user.username)
        user.username = new_username
        user.save()
        return redirect('nic_app:home')
    return render(request, 'change_username.html')


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def discussion(request):
    return render(request, 'discussion.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def tutorial(request):
    return render(request, 'tutorial.html')


def user(request):
    return render(request, 'user.html')


@login_required(login_url='/login')
def cart(request):
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to view this page.")
        return redirect('login')

    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total_price = 0
    total_quantity = 0
    for item in cart_items:
        total_price += item.item.price*item.quantity
        total_quantity += item.quantity

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_quantity': total_quantity, 'total_price': total_price})


@login_required(login_url='/login')
def add_to_cart(request, pk):
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to view this page.")
        return redirect('login')

    obj = Project.objects.get(pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=obj)
    cart_item.quantity += 1
    cart_item.save()

    messages.success(request, f'{obj.name} added to cart.')
    return redirect(request.META.get('HTTP_REFERER', '/'))

    # carts=Cart.objects.get(user=request.user)
    # return render(request, 'cart.html',{'cart':carts})


@login_required(login_url='/login')
def remove_from_cart(request, pk):
    if not request.user.is_authenticated:
        messages.info(request, "You must be logged in to view this page.")
        return redirect('login')

    obj = Project.objects.get(pk=pk)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, item=obj)
    cart_item.quantity -= 1
    if cart_item.quantity == 0:
        cart_item.delete()
    else:
        cart_item.save()
    messages.success(request, f'{obj.name} removed from cart.')
    return redirect(request.META.get('HTTP_REFERER', '/'))

    # carts=Cart.objects.get(user=request.user)
    # return render(request, 'cart.html',{'cart':carts})



def item(request, pk):
    item=Project.objects.get(pk=pk)
    return render(request, 'item.html', {'item':item})

@login_required(login_url='/login')
def buy(request, pk):
    item=Project.objects.get(pk=pk)
    return render(request, 'buy.html', {'item':item})

def partner_schools(request):
    return render(request, 'partner_schools.html')