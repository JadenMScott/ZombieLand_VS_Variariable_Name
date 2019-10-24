from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

import bcrypt

def index(request):
    return redirect('/login')

def logout(request):
    request.session.clear()
    return redirect('/login')

def login(request):
    if request.method == "GET":
        return render(request, 'login_handler/needs_revision')
    elif request.method == "POST":
        # this is the email of the user that is put into the login page
        user = Users.objects.filter(email=request.POST['needs_revision'])
        if len(user) > 0:
            testpass = user.first().password
            # password field from the login page
            if bcrypt.checkpw((request.POST['needs_revision']).encode(), testpass.encode()):
                # this is the user put in the login username field 
                request.session['user'] = Users.objects.get(email=request.POST['needs_revision']).id
                return redirect('/needs_revision')
            else:
                messages.error(request, 'Incorrect Credentials')
                return redirect('/needs_revision')

def register(request):
    errors = Users.objects.Pass_validator(request.POST)
    if len(errors) > 0:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        # password for the registration page
        print(request.POST['needs_revision'])
        passw = request.POST['needs_revision']
        pw_hash = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
        print(pw_hash)
        # this is creating the user so pretty much just read the tag its creating and put in the info needed
        Users.objects.create(email=request.POST['needs_revision'], phone=request.P password=pw_hash, first_name=request.POST['needs_revision'], last_name=request.POST['needs_revision']) 
        return redirect("/login")

