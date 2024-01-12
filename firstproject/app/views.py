from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
            return redirect('login')
    return render(request, "login.html")


def registeration(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('registration')

            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                              email=email, password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "password is not matching")
            return redirect('registration')
            return redirect('/')
    return render(request, "app1.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
