from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from . form import FormEntryForm

def show_form(request):
    form = FormEntryForm()
    return render(request, 'form.html', {'form': form})

def submit_form(request):
    if request.method == 'POST':
        form = FormEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order Placed........")
            return redirect('form')
        print("created")
    else:
        form = FormEntryForm()
    return render(request, 'form.html', {'form': form})

# Create your views here.

def home(request):
    return render(request,'index.html')
def profile(request):
    return render(request,'profile.html')
# def form(request):
#     return render(request,'form.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
