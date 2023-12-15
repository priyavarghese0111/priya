
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.urls import reverse


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.error(request,"Invalid credentials")
            return redirect(reverse('credentials:login'))
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username =request.POST.get('username','')
        password = request.POST.get('password','')
        cpassword = request.POST.get('confirmpassword','')

        if password == cpassword :
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username already taken")
                return redirect(reverse('credentials:register'))

            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                print("user created")
                return redirect(reverse('credentials:login'))
        else:
            messages.error(request,"password not matching")
            return redirect(reverse('credentials:register'))


    return render (request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')