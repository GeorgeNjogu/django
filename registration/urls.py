from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registerepage/',views.mypage,name='firstpage'),
    path('home/', views.home, name='Home'),
    path('register/', views.register, name='Register'),
    path('login/', views.login, name='Login'),
    path('courses/', views.courses, name='Courses'),
]
