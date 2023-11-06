
from django.contrib import admin
from django.urls import path
from AMS_APP import views

urlpatterns = [
    path('AdminLogin', views.AdminLogin, name='Admin_Login'),
    path('StudentLogin', views.StudentLogin, name='Student_Login'),
    path('TeacherLogin', views.TeacherLogin, name='Teacher_Login'),\
    path('addnewstudent', views.addnewstudent, name='addnewstudent'),
    path('AdminDashboard', views.AdminDashboard, name='AdminDashboard'),
    path('class_mgmt/', views.class_mgmt, name='class_mgmt/'),
    path('courseadd', views.courseadd, name='courseadd'),
    path('', views.index, name='index'),
    path('student_mgmt/', views.student_mgmt, name='student_mgmt'),
    path('teacher_mgmt/', views.teacher_mgmt, name='teacher_mgmt'),
    path('teacher', views.teacher, name='teacher'),
    path('viewclass', views.viewclass, name='viewclass'),
    path('viewfaculty', views.viewfaculty, name='viewfaculty'),
    path('viewstudent', views.viewstudent, name='viewstudent'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
]

