
from django.contrib import admin
from django.urls import path
from AMS_APP import views

urlpatterns = [
    path('AdminLogin', views.AdminLogin, name='Admin_Login'),
    path('Studentlogin', views.Studentlogin, name='Student_Login'),
    path('TeacherLogin', views.TeacherLogin, name='Teacher_Login'),
    path('login', views.loginuser, name='login'),
]

