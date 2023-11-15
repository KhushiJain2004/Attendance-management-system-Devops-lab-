from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from AMS_APP.models import Teacher,Student,Subject
from django.contrib.auth.models import User
from django.contrib import messages

def AdminLogin(request):
    if not request.user.is_anonymous:
        return redirect("/AdminDashboard")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('AdminDashboard')
        return render(request, 'AdminLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'AdminLogin.html')

def StudentLogin(request):
    if not request.user.is_anonymous:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print('hi')

        if user is not None:
            login(request, user)
            return redirect('')
        return render(request, 'Studentlogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'Studentlogin.html')

def TeacherLogin(request):
    if not request.user.is_anonymous:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('teacher_dashboard')
        return render(request, 'TeacherLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'TeacherLogin.html')

# def loginuser(request):
#     if not request.user.is_anonymous:
#             return redirect('/')
#     if request.method=="POST":
#         username=request.POST.get('ID')
#         password=request.POST.get('password')
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             login(request,user)
#             return redirect('/admindashboard')              #change dashboard according to where it is coming from
#         else:
#             messages.error(request, 'Wrong username or password')
#             return render(request,'login.html')               #change login.html
#     return render(request,'login.html')                       #change login.html
    
def addnewstudent(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method=='POST':

        student_id='S'+str(len(Student.objects.all())+10000)
        student_name=request.POST.get('student_name')
        email_id=request.POST.get('emailid')
        password=request.POST.get('password')
        student=Student(student_id=student_id,student_name=student_name,email_id=email_id,password=password)
        student.save()

        user = User.objects.create_user(username=student_id, email=email_id, first_name=student_name, last_name='Student', password=password)
        user.save()
        messages.success(request, f'New Student {student_name} with ID {student_id} is added' ,extra_tags='posted')
    return render(request, 'addnewstudent.html')


def AdminDashboard(request):
    return render(request, 'AdminDashboard.html')

def class_mgmt(request):
    subject_id = request.GET.get('subject_id')
    
    if request.method=='POST':
        classes_held=Subject.objects.filter(subject_id=subject_id)[0].classes_held
        student_id=request.POST.get('student_id')
        student=Student.objects.filter(student_id=student_id)
        if student[0].class1=='':
            student.update(class1=subject_id)
            student.update(class1_att=classes_held*'-')
        elif student[0].class2=='':
            student.update(class2=subject_id)
            student.update(class2_att=classes_held*'-')
        elif student[0].class3=='':
            student.update(class3=subject_id)
            student.update(class3_att=classes_held*'-')
        elif student[0].class4=='':
            student.update(class4=subject_id)
            student.update(class4_att=classes_held*'-')
        elif student[0].class5=='':
            student.update(class5=subject_id)
            student.update(class5_att=classes_held*'-')
        elif student[0].class6=='':
            student.update(class6=subject_id)
            student.update(class6_att=classes_held*'-')
        elif student[0].class7=='':
            student.update(class7=subject_id)
            student.update(class7_att=classes_held*'-')
        else:
            student.update(class8=subject_id)
            student.update(class8_att=classes_held*'-')

        numofstudents=int(Subject.objects.filter(subject_id=subject_id)[0].number_of_students)+1
        print(numofstudents)
        Subject.objects.filter(subject_id=subject_id).update(number_of_students=numofstudents)
    
    
    
    
    classs=list(Subject.objects.filter(subject_id=subject_id))[0]
    class_name=classs.subject_name
    teacher_id=classs.teacher_id
    teacher_name=Teacher.objects.filter(teacher_id=teacher_id)[0].teacher_name
    student_list=list(Student.objects.filter(class1=subject_id))+list(Student.objects.filter(class2=subject_id))+list(Student.objects.filter(class3=subject_id))+list(Student.objects.filter(class4=subject_id))+list(Student.objects.filter(class5=subject_id))+list(Student.objects.filter(class6=subject_id))+list(Student.objects.filter(class7=subject_id))+list(Student.objects.filter(class8=subject_id))
    
    dic={'class_id':subject_id,'student_list':student_list,'class_name':class_name,'teacher_id':teacher_id,'teacher_name':teacher_name}
    return render(request, 'class_mgmt.html',dic)

def courseadd(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method=='POST':

        subject_id='C'+str(len(Subject.objects.all())+10000)
        subject_name=request.POST.get('courseName')
        teacher_id=request.POST.get('teacherid')
        subject=Subject(subject_id=subject_id,subject_name=subject_name,teacher_id=teacher_id,classes_held=0,number_of_students=0)
        subject.save()

        
        messages.success(request, f'New Subject {subject_name} with teacher {teacher_id} is added' ,extra_tags='posted')
    return render(request, 'courseadd.html')

def index(request):
    return render(request, 'index.html')

def student_mgmt(request):
    return render(request, 'student_mgmt.html')

def teacher_mgmt(request):
    return render(request, 'teacher_mgmt.html')

def teacher(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method=='POST':

        teacher_id='T'+str(len(Teacher.objects.all())+10000)
        teacher_name=request.POST.get('teacherName')
        email_id=request.POST.get('emailid')
        password=request.POST.get('password')
        teacher=Teacher(teacher_id=teacher_id,teacher_name=teacher_name,email_id=email_id,password=password)
        teacher.save()

        user = User.objects.create_user(username=teacher_id, email=email_id, first_name=teacher_name, last_name='Teacher', password=password)
        user.save()
        messages.success(request, f'New teacher {teacher_name} with ID {teacher_id} is added' ,extra_tags='posted')
    return render(request, 'teacher.html')

def viewclass(request):
    if request.user.is_anonymous:
        return redirect("/")
    subject_list=(Subject.objects.all())
    return render(request, 'viewclass.html',
                  {'subject_list':subject_list})

def viewfaculty(request):
    if request.user.is_anonymous:
        return redirect("/")
    teacher_list=(Teacher.objects.all())
    return render(request, 'viewfaculty.html',
                  {'teacher_list':teacher_list})

def viewstudent(request):
    if request.user.is_anonymous:
        return redirect("/")
    student_list=(Student.objects.all())
    return render(request, 'viewstudent.html',
                  {'student_list':student_list})

def logoutuser(request):
    logout(request)
    return redirect('/')


