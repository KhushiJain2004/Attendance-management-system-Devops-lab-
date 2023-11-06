from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'AdminLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'AdminLogin.html')

def Studentlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        return render(request, 'Studentlogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'Studentlogin.html')

def TeacherLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('teacher_dashboard')
        return render(request, 'TeacherLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'TeacherLogin.html')

def loginuser(request):
    if not request.user.is_anonymous:
            return redirect('/')
    if request.method=="POST":
        username=request.POST.get('ID')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/admindashboard')              #change dashboard according to where it is coming from
        else:
            messages.error(request, 'Wrong username or password')
            return render(request,'login.html')               #change login.html
    return render(request,'login.html')                       #change login.html
    
def addnewstudent(request):
    if request.method == 'POST':
        student_name = request.POST.get('student')
        student_id = request.POST.get('studentName')
        password = request.POST.get('password')

        return HttpResponse('Student added successfully')
    else:
        return render(request, 'addnewstudent.html')


def AdminDashboard(request):
    context = {
        # Add any context data you want to pass to the template here
    }

    return render(request, 'AdminDashboard.html', context)

def class_mgmt(request):
    context = {
        # You can add any context data you want to pass to the template here
    }
    return render(request, 'class_mgmt.html', context)

def courseadd(request):
    context = {
        # You can add any context data you want to pass to the template here
    }
    return render(request, 'courseadd.html', context)

def index(request):
    context = {
        # You can add any context data you want to pass to the template here
    }
    return render(request, 'index.html', context)

def student_mgmt(request):
    context = {
       
    }
    return render(request, 'student_mgmt.html', context)

def teacher_mgmt(request):
    context = {
       
    }
    return render(request, 'teacher_mgmt.html', context)

def teacher(request):
    context = {
        # You can add any context data you want to pass to the template here
    }
    return render(request, 'teacher.html', context)

def viewclass(request):
    context = {
        # You can add any context data you want to pass to the template here
    }
    return render(request, 'viewclass.html', context)

def viewfaculty(request):
    context = {
        # You can add any context data you want to pass to the template here
    }
    return render(request, 'viewfaculty.html', context)

def viewstudent(request):
    context = {
        # You can add any context data you want to pass to the template here
    }
    return render(request, 'viewstudent.html', context)


