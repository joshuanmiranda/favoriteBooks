from django.shortcuts import render, redirect, HttpResponse
from .models import *
from RegLoginApp.models import *
from django.contrib import messages
import bcrypt

def index(request):
    context = {
        'user': User.objects.get(id=request.session['user']),
        'allBooks': Book.objects.all(),
    }
    return render(request, 'book.html', context)

def create(request):
    if request.method=="POST":
        loggedUser = User.objects.get(id=request.session['user'])
        newBook = Book.objects.create(title=request.POST['title'], description=request.POST['description'], uploaded_by=loggedUser)
        return redirect('/books')
    return redirect('/books')
