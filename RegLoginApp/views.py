from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'RegLog.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        hashedPW = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        FirstName = request.POST['first_name']
        LastName = request.POST['last_name']
        EmailAddress = request.POST['email_address']
        Password = hashedPW
        new_user = User.objects.create(first_name=FirstName, last_name=LastName, email_address=EmailAddress, password=Password)
        request.session['user'] = User.objects.last().id
        return redirect('/books')

def login(request):
    if request.method == "POST":
        errors = User.objects.log_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        request.session['user'] = User.objects.get(email_address=request.POST['log_email']).id
        return redirect('/books')

def success(request):
    pass
    return render(request, 'Success.html')

def logout(request):
    request.session.flush()
    return redirect('/')