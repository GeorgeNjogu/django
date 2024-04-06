from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader #for routing your templates
def registration(request):
    return HttpResponse("Welcome to Registration")

def mypage(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())








