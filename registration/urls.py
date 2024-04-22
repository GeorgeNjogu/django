from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registerepage/',views.mypage,name='firstpage'),
    path('home/', views.home, name='Home'),
    path('', views.register, name='Register'),
    path('login/', views.login, name='Login'),
    path('courses/', views.courses, name='Courses'),
    path('register/', views.register, name='myregistration'),

    path('addstudent',views.addstudent, name='addstudent'),
    path('editstudent',views.editstudent, name='editstudent'),
    path('updatestudent',views.updatestudent, name='updatestudent'),

    path('deletestudent/<id>',views.deletestudent)

    ]



