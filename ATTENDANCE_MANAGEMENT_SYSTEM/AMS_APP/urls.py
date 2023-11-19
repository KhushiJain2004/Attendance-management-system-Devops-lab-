
from django.contrib import admin
from django.urls import path
from AMS_APP import views

urlpatterns = [
    path('addnewstudent', views.addnewstudent, name='addnewstudent'),
    path('AdminDashboard', views.AdminDashboard, name='AdminDashboard'),
    path('AdminLogin', views.AdminLogin, name='Admin_Login'),
    path('attendancesummary/', views.attendancesummary, name='attendancesummary'),
    path('class_mgmt/', views.class_mgmt, name='class_mgmt/'),
    path('courseadd', views.courseadd, name='courseadd'),
    path('', views.index, name='index'),
    path('markStudentAttendance/', views.markStudentAttendance, name='markStudentAttendance'),
    path('student_mgmt/', views.student_mgmt, name='student_mgmt'),
    path('Studentdashboard', views.Studentdashboard, name='Studentdashboard'),
    path('StudentLogin', views.StudentLogin, name='Student_Login'),
    path('studentprofile/', views.studentprofile, name='studentprofile'),
    path('teach',views.teach, name='teach'),
    path('teacher_mgmt/', views.teacher_mgmt, name='teacher_mgmt'),
    path('teacher', views.teacher, name='teacher'),
    path('teacherdas/', views.teacherdas, name='teacherdas'),
    path('teacherdashboard', views.teacherdashboard, name='teacherdashboard'),
    path('TeacherLogin', views.TeacherLogin, name='Teacher_Login'),
    path('viewattendancepageforstudent/', views.viewattendancepageforstudent, name='viewattendancepageforstudent'),
    path('viewclass', views.viewclass, name='viewclass'),
    path('viewfaculty', views.viewfaculty, name='viewfaculty'),
    path('viewstudent', views.viewstudent, name='viewstudent'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('coursename', views.coursename, name='coursename'),
]

