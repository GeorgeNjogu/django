from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader #for routing your templates
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from  .models import Student
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
    mydata = Student.objects.all()
    context = {'data': mydata}
    return render(request, 'register.html', context)


@csrf_exempt
def addstudent(request):
   if request.method == 'POST':
     name = request.POST.get('fname')
     email = request.POST.get('Email')

     mydata = {'name': name, 'email': email}#this is to check wheteher
                                            # your urls and functions are getting info by displaying on the terminal
     print(mydata)

     obj1=Student(first_name=name,email=email,)
     obj1.save()

     mydata = Student.objects.all()
     context = {'data': mydata}
     return render(request, 'register.html',context)

def editstudent(request,id):
  data = Student.objects.get(id=id)
  context = {'data': data}
  return render(request, 'updatestudent.html', context)

def updatestudent(request,id):
   if request.method == 'POST':
       name = request.POST.get('fname')
       email = request.POST.get('email')

       editstudent = Student.objects.get(id=id)
       editstudent.first_name = name
       editstudent.email = email
   return redirect('/register')

def deletestudent(request,id):
   deletestudent = Student.objects.get(id=id)
   deletestudent.delete()
   return redirect('/register')








