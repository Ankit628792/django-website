from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate

# Create your views here.

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully.')
    return render(request, 'contact.html')

def index(request):
    # if request.user.is_anonymous:
    #     return redirect('/login')
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect("/")
        else:
            return render(request,'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')