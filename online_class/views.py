from django.shortcuts import render
from django.http import HttpResponse  # can be removed(no longer required.)

def home(request):
	return render(request,'online_class/home.html',{'title': 'Home'})

def about(request):
	return render(request,'online_class/about.html',{'title': 'About'})

def index(request):
	return render(request,'online_class/index.html',{'title': 'Sign-In'})
