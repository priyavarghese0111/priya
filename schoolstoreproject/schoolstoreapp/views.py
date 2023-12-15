from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request,'home.html')

def purchase(request):
    return render(request,'purchase.html')

def order(request):
    return render(request,'order.html')