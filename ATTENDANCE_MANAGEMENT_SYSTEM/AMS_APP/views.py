from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from AMS_APP.models import Teacher,Student,Subject
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

def AdminLogin(request):
    if not request.user.is_anonymous:
        return redirect("/AdminDashboard")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if 'T' in username or 'S' in username:
            return redirect('/')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('AdminDashboard')
        return render(request, 'AdminLogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'AdminLogin.html')

def StudentLogin(request):
    if not request.user.is_anonymous:
        return redirect("Studentdashboard")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if 'S' not in username:
            return redirect('/')
        user = authenticate(request, username=username, password=password)
        # print('hi')

        if user is not None:
            login(request, user)
            return redirect('Studentdashboard')
        return render(request, 'Studentlogin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'Studentlogin.html')

def TeacherLogin(request):
    if not request.user.is_anonymous:
        return redirect("teacherdashboard")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if 'T' not in username:
            return redirect('/')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('teacherdashboard')
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
        if list(Student.objects.all())==[]:
            student_id='S10000'
        else:
            prev_student_id=list(Student.objects.all())[-1].student_id
            student_id='S'+str(int(prev_student_id[1:])+1)
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
    user=request.user.username
    if 'S1' in user:
        return redirect('/Studentdashboard')
    elif 'T1' in user:
        return redirect('/teacherdashboard')
    num_student=len(Student.objects.all())
    num_teacher=len(Teacher.objects.all())
    num_class=len(Subject.objects.all())
    dic={'num_student':num_student,'num_teacher':num_teacher,'num_class':num_class}
    return render(request, 'AdminDashboard.html',dic)

def class_mgmt(request):
    subject_id = request.GET.get('subject_id')
    
    if request.method=='POST':
        classes_held=Subject.objects.filter(subject_id=subject_id)[0].classes_held
        student_id=request.POST.get('student_id')
        student=Student.objects.filter(student_id=student_id)
        if list(student)==[]:
            messages.error(request, 'Student does not exist')
        elif student[0].class1==subject_id or student[0].class2==subject_id or student[0].class3==subject_id or student[0].class4==subject_id or student[0].class5==subject_id or student[0].class6==subject_id or student[0].class7==subject_id or student[0].class8==subject_id:
            messages.error(request, 'Student already in class')
        elif student[0].class1=='':
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
    # student_list=list(Student.objects.filter(class1=subject_id))+list(Student.objects.filter(class2=subject_id))+list(Student.objects.filter(class3=subject_id))+list(Student.objects.filter(class4=subject_id))+list(Student.objects.filter(class5=subject_id))+list(Student.objects.filter(class6=subject_id))+list(Student.objects.filter(class7=subject_id))+list(Student.objects.filter(class8=subject_id))
    
    student_list=list(Student.objects.filter(class1=subject_id))+list(Student.objects.filter(class2=subject_id))+list(Student.objects.filter(class3=subject_id))+list(Student.objects.filter(class4=subject_id))+list(Student.objects.filter(class5=subject_id))+list(Student.objects.filter(class6=subject_id))+list(Student.objects.filter(class7=subject_id))+list(Student.objects.filter(class8=subject_id))    
    student_list_new=[]
    for i in student_list:
        id=i.student_id
        name=i.student_name

        if i.class1==subject_id:
            att_str=i.class1_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class2==subject_id:
            att_str=i.class2_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class3==subject_id:
            att_str=i.class3_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class4==subject_id:
            att_str=i.class4_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class5==subject_id:
            att_str=i.class5_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class6==subject_id:
            att_str=i.class6_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class7==subject_id:
            att_str=i.class7_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class8==subject_id:
            att_str=i.class8_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        student_list_new.append(stud_dic)

    dic={'class_id':subject_id,'class_name':class_name,'teacher_id':teacher_id,'teacher_name':teacher_name,'student_list':student_list_new}
    return render(request, 'class_mgmt.html',dic)

def courseadd(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method=='POST':
        if list(Subject.objects.all())==[]:
            subject_id='C10000'
        else:
            prev_subject_id=list(Subject.objects.all())[-1].subject_id
            subject_id='C'+str(int(prev_subject_id[1:])+1)
        subject_name=request.POST.get('courseName')
        teacher_id=request.POST.get('teacherid')
        subject=Subject(subject_id=subject_id,subject_name=subject_name,teacher_id=teacher_id,classes_held=0,number_of_students=0)
        subject.save()

        
        messages.success(request, f'New Subject {subject_name} with teacher {teacher_id} is added' ,extra_tags='posted')
    return render(request, 'courseadd.html')

def index(request):
    return render(request, 'index.html')

def student_mgmt(request):
    student_id = request.GET.get('student_id')
    student=Student.objects.filter(student_id=student_id)[0]

    student_name=student.student_name
    class_list=[]
    if student.class1!='':
        a=[student.class1]
        att_str=student.class1_att
        if att_str.count('P')==0 and att_str.count('A')==0:
            att='NA'
        else:
            att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
        a.append(att)
        class_list.append(a)
        if student.class2!='':
            a=[student.class2]
            att_str=student.class2_att
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            a.append(att)
            class_list.append(a)
            if student.class3!='':
                a=[student.class3]
                att_str=student.class3_att
                if att_str.count('P')==0 and att_str.count('A')==0:
                    att='NA'
                else:
                    att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                a.append(att)
                class_list.append(a)
                if student.class4!='':
                    a=[student.class4]
                    att_str=student.class4_att
                    if att_str.count('P')==0 and att_str.count('A')==0:
                        att='NA'
                    else:
                        att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                    a.append(att)
                    class_list.append(a)
                    if student.class5!='':
                        a=[student.class5]
                        att_str=student.class5_att
                        if att_str.count('P')==0 and att_str.count('A')==0:
                            att='NA'
                        else:
                            att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                        a.append(att)
                        class_list.append(a)
                        if student.class6!='':
                            a=[student.class6]
                            att_str=student.class6_att
                            if att_str.count('P')==0 and att_str.count('A')==0:
                                att='NA'
                            else:
                                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                            a.append(att)
                            class_list.append(a)
                            if student.class7!='':
                                a=[student.class7]
                                att_str=student.class7_att
                                if att_str.count('P')==0 and att_str.count('A')==0:
                                    att='NA'
                                else:
                                    att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                                a.append(att)
                                class_list.append(a)
                                if student.class8!='':
                                    a=[student.class8]
                                    att_str=student.class8_att
                                    if att_str.count('P')==0 and att_str.count('A')==0:
                                        att='NA'
                                    else:
                                        att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                                    a.append(att)
                                    class_list.append(a)
    
    dic={'student_name':student_name,'student_id':student_id,'class_list':class_list}
    return render(request, 'student_mgmt.html',dic)

def teacher_mgmt(request):
    teacher_id = request.GET.get('teacher_id')
    print(teacher_id)
    teacher_name=Teacher.objects.filter(teacher_id=teacher_id)[0].teacher_name
    class_list=list(Subject.objects.filter(teacher_id=teacher_id))

    dic={'teacher_name':teacher_name,'class_list':class_list}
    return render(request, 'teacher_mgmt.html',dic)

def teacher(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method=='POST':
        if list(Teacher.objects.all())==[]:
            teacher_id='T10000'
        else:
            prev_teacher_id=list(Teacher.objects.all())[-1].teacher_id
            teacher_id='T'+str(int(prev_teacher_id[1:])+1)
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

def attendancesummary(request):
    student_id = request.user.username
    student=Student.objects.filter(student_id=student_id)[0]

    student_name=student.student_name
    class_list=[]
    if student.class1!='':
        a=[student.class1]
        att_str=student.class1_att
        if att_str.count('P')==0 and att_str.count('A')==0:
            att='NA'
        else:
            att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
        class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
        a.append(att)
        a.append(class_name)
        class_list.append(a)
        if student.class2!='':
            a=[student.class2]
            att_str=student.class2_att
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            class_name=Subject.objects.filter(subject_id=student.class2)[0].subject_name
            a.append(att)
            a.append(class_name)
            class_list.append(a)
            if student.class3!='':
                a=[student.class3]
                att_str=student.class3_att
                if att_str.count('P')==0 and att_str.count('A')==0:
                    att='NA'
                else:
                    att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                a.append(att)
                a.append(class_name)
                class_list.append(a)
                if student.class4!='':
                    a=[student.class4]
                    att_str=student.class4_att
                    if att_str.count('P')==0 and att_str.count('A')==0:
                        att='NA'
                    else:
                        att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                    class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                    a.append(att)
                    a.append(class_name)
                    class_list.append(a)
                    if student.class5!='':
                        a=[student.class5]
                        att_str=student.class5_att
                        if att_str.count('P')==0 and att_str.count('A')==0:
                            att='NA'
                        else:
                            att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                        class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                        a.append(att)
                        a.append(class_name)
                        class_list.append(a)
                        if student.class6!='':
                            a=[student.class6]
                            att_str=student.class6_att
                            if att_str.count('P')==0 and att_str.count('A')==0:
                                att='NA'
                            else:
                                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                            class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                            a.append(att)
                            a.append(class_name)
                            class_list.append(a)
                            if student.class7!='':
                                a=[student.class7]
                                att_str=student.class7_att
                                if att_str.count('P')==0 and att_str.count('A')==0:
                                    att='NA'
                                else:
                                    att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                                class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                                a.append(att)
                                a.append(class_name)
                                class_list.append(a)
                                if student.class8!='':
                                    a=[student.class8]
                                    att_str=student.class8_att
                                    if att_str.count('P')==0 and att_str.count('A')==0:
                                        att='NA'
                                    else:
                                        att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                                    class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                                    a.append(att)
                                    a.append(class_name)
                                    class_list.append(a)



    dic={'student_name':student_name,'student_id':student_id,'class_list':class_list}
    return render(request, 'attendancesummary.html', dic)

def markStudentAttendance(request):
    if request.method == 'POST':
        subject_id= request.GET.get('subject_id')
        sub=Subject.objects.filter(subject_id=subject_id)[0]
        sub.classes_held+=1
        date=datetime.today().strftime('%Y-%m-%d')
        sub.class_info+=','+ datetime.today().strftime('%Y-%m-%d')
        sub.save()
        student_list=list(Student.objects.filter(class1=subject_id))+list(Student.objects.filter(class2=subject_id))+list(Student.objects.filter(class3=subject_id))+list(Student.objects.filter(class4=subject_id))+list(Student.objects.filter(class5=subject_id))+list(Student.objects.filter(class6=subject_id))+list(Student.objects.filter(class7=subject_id))+list(Student.objects.filter(class8=subject_id))
        for i in student_list:
            value=request.POST.get(i.student_id)
            if i.class1==subject_id:
                i.class1_att+=value
                i.save()
            elif i.class2==subject_id:
                i.class2_att+=value
                i.save()
            elif i.class3==subject_id:
                i.class3_att+=value
                i.save()
            elif i.class4==subject_id:
                i.class4_att+=value
                i.save()
            elif i.class5==subject_id:
                i.class5_att+=value
                i.save()
            elif i.class6==subject_id:
                i.class6_att+=value
                i.save()
            elif i.class7==subject_id:
                i.class7_att+=value
                i.save()
            elif i.class8==subject_id:
                i.class8_att+=value
                i.save()
        
        return redirect('/teach')
            

    subject_id= request.GET.get('subject_id')
    student_list=list(Student.objects.filter(class1=subject_id))+list(Student.objects.filter(class2=subject_id))+list(Student.objects.filter(class3=subject_id))+list(Student.objects.filter(class4=subject_id))+list(Student.objects.filter(class5=subject_id))+list(Student.objects.filter(class6=subject_id))+list(Student.objects.filter(class7=subject_id))+list(Student.objects.filter(class8=subject_id))
    dic={'student_list':student_list,'subject_id':subject_id}
    return render(request, 'markStudentAttendance.html',dic)

def Studentdashboard(request):
    if 'S' not in request.user.username:
        redirect('/')
    student_id = request.user.username
    student=Student.objects.filter(student_id=student_id)[0]

    student_name=student.student_name
    class_list=[]
    if student.class1!='':
        a=[student.class1]
        att_str=student.class1_att
        if att_str.count('P')==0 and att_str.count('A')==0:
            att='NA'
        else:
            att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
        class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
        a.append(att)
        a.append(class_name)
        class_list.append(a)
        if student.class2!='':
            a=[student.class2]
            att_str=student.class2_att
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            class_name=Subject.objects.filter(subject_id=student.class2)[0].subject_name
            a.append(att)
            a.append(class_name)
            class_list.append(a)
            if student.class3!='':
                a=[student.class3]
                att_str=student.class3_att
                if att_str.count('P')==0 and att_str.count('A')==0:
                    att='NA'
                else:
                    att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                a.append(att)
                a.append(class_name)
                class_list.append(a)
                if student.class4!='':
                    a=[student.class4]
                    att_str=student.class4_att
                    if att_str.count('P')==0 and att_str.count('A')==0:
                        att='NA'
                    else:
                        att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                    class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                    a.append(att)
                    a.append(class_name)
                    class_list.append(a)
                    if student.class5!='':
                        a=[student.class5]
                        att_str=student.class5_att
                        if att_str.count('P')==0 and att_str.count('A')==0:
                            att='NA'
                        else:
                            att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                        class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                        a.append(att)
                        a.append(class_name)
                        class_list.append(a)
                        if student.class6!='':
                            a=[student.class6]
                            att_str=student.class6_att
                            if att_str.count('P')==0 and att_str.count('A')==0:
                                att='NA'
                            else:
                                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                            class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                            a.append(att)
                            a.append(class_name)
                            class_list.append(a)
                            if student.class7!='':
                                a=[student.class7]
                                att_str=student.class7_att
                                if att_str.count('P')==0 and att_str.count('A')==0:
                                    att='NA'
                                else:
                                    att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                                class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                                a.append(att)
                                a.append(class_name)
                                class_list.append(a)
                                if student.class8!='':
                                    a=[student.class8]
                                    att_str=student.class8_att
                                    if att_str.count('P')==0 and att_str.count('A')==0:
                                        att='NA'
                                    else:
                                        att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
                                    class_name=Subject.objects.filter(subject_id=student.class1)[0].subject_name
                                    a.append(att)
                                    a.append(class_name)
                                    class_list.append(a)



    dic={'student_name':student_name,'student_id':student_id,'class_list':class_list}
    return render(request, 'Studentdashboard.html',dic)

def studentprofile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        courses = request.POST.getlist('courses')


    return render(request, 'studentprofile.html')

def teach(request):
    if request.user.is_anonymous:
        return redirect("/")
    else:
        ruser=request.user.username
        if 'S' in ruser:
            return redirect('/studentdashboard')
        elif ('T' not in ruser) and ('akshit'!=ruser):
            return redirect('/admindashboard')
    teacher_id=request.user.username
    class_list=list(Subject.objects.filter(teacher_id=teacher_id))
    dic={'class_list':class_list}
    return render(request, 'teach.html',dic)

def teacherdas(request):
    subject_id= request.GET.get('subject_id')
    subject_name=Subject.objects.filter(subject_id=subject_id)[0].subject_name
    sub=Subject.objects.filter(subject_id=subject_id)[0]
    date=sub.class_info.split(',')
    date.pop(0)


    student_list=list(Student.objects.filter(class1=subject_id))+list(Student.objects.filter(class2=subject_id))+list(Student.objects.filter(class3=subject_id))+list(Student.objects.filter(class4=subject_id))+list(Student.objects.filter(class5=subject_id))+list(Student.objects.filter(class6=subject_id))+list(Student.objects.filter(class7=subject_id))+list(Student.objects.filter(class8=subject_id))    
    student_list_new=[]
    for i in student_list:
        id=i.student_id
        name=i.student_name

        if i.class1==subject_id:
            att_str=i.class1_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class2==subject_id:
            att_str=i.class2_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class3==subject_id:
            att_str=i.class3_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class4==subject_id:
            att_str=i.class4_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class5==subject_id:
            att_str=i.class5_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class6==subject_id:
            att_str=i.class6_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class7==subject_id:
            att_str=i.class7_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        elif i.class8==subject_id:
            att_str=i.class8_att
            att_list=att_str
            if att_str.count('P')==0 and att_str.count('A')==0:
                att='NA'
            else:
                att=att_str.count('P')/(att_str.count('P')+att_str.count('A'))*100
            stud_dic={'id':id,'name':name,'att':att,'att_list':att_list}

        student_list_new.append(stud_dic)

    dic={'date':date,'subject_id':subject_id,'subject_name':subject_name,'student_list':student_list_new}
    return render(request, 'teacherdas.html',dic)

def teacherdashboard(request):
    if 'T' not in request.user.username:
        redirect('/')
    teacher_id=request.user.username
    classes=list(Subject.objects.filter(teacher_id=teacher_id))
    num_classes=len(classes)
    num_students=0
    for i in classes:
        num_students+=i.number_of_students
    dic={'num_classes':num_classes,'num_students':num_students}
    return render(request, 'teacherdashboard.html',dic)

def viewattendancepageforstudent(request):
    subject_id=request.GET.get('subject_id')
    student_id = request.user.username
    sub=Subject.objects.filter(subject_id=subject_id)[0]
    date=sub.class_info.split(',')
    if len(date)!=0:
        date.pop(0)

    i=Student.objects.filter(student_id=student_id)[0]
    if i.class1==subject_id:
            att_str=i.class1_att
            att_list=list(att_str)
    elif i.class2==subject_id:
            att_str=i.class2_att
            att_list=list(att_str)
    elif i.class3==subject_id:
            att_str=i.class3_att
            att_list=list(att_str)
    elif i.class4==subject_id:
            att_str=i.class4_att
            att_list=list(att_str)
    elif i.class5==subject_id:
            att_str=i.class5_att
            att_list=list(att_str)
    elif i.class6==subject_id:
            att_str=i.class6_att
            att_list=list(att_str)
    elif i.class7==subject_id:
            att_str=i.class7_att
            att_list=list(att_str)
    elif i.class8==subject_id:
            att_str=i.class8_att
            att_list=list(att_str)
    date_att_list=[]
    for i in range(len(att_list)):
        z=[date[i],att_list[i]]
        date_att_list.append(z)

    dic={'date_att_list':date_att_list}
    print(date_att_list)
    return render(request, 'viewattendancepageforstudent.html',dic)

def coursename(request):
    return render(request, 'coursename.html')

def remove(request):
    remove = request.GET.get('remove')
    subject_id=remove[0:6]
    student_id=remove[6:]
    i=Student.objects.filter(student_id=student_id)[0]
    if i.class1==subject_id:
            i.class1_att=''
            i.class1=''
    elif i.class2==subject_id:
            i.class2_att=''
            i.class2=''
    elif i.class3==subject_id:
            i.class3_att=''
            i.class3=''
    elif i.class4==subject_id:
            i.class4_att=''
            i.class4=''
    elif i.class5==subject_id:
            i.class5_att=''
            i.class5=''
    elif i.class6==subject_id:
            i.class6_att=''
            i.class6=''
    elif i.class7==subject_id:
            i.class7_att=''
            i.class7=''
    elif i.class8==subject_id:
            i.class8_att=''
            i.class8=''
    i.save()
    sub=Subject.objects.filter(subject_id=subject_id)[0]
    sub.number_of_students=int(sub.number_of_students)-1
    sub.save()
    return redirect(f'/class_mgmt/?subject_id={subject_id}')

def removestudent(request):
    student_id=request.GET.get('student_id')
    user=User.objects.get(username = student_id)
    user.delete()
    user=Student.objects.filter(student_id=student_id)[0]
    user.delete()
    return redirect('/viewstudent')

def editattendance(request):
    if request.method == 'POST':
        details=request.GET.get('details')
        subject_id=details[0:6]
        student_id=details[6:]
        sub=Subject.objects.filter(subject_id=subject_id)[0]
        date=sub.class_info.split(',')
        if len(date)!=0:
            date.pop(0)

        att=''
        for j in range(len(date)):
            value=request.POST.get(str(j))
            print(value)
            att+=value
        
        i=Student.objects.filter(student_id=student_id)[0]
            
        if i.class1==subject_id:
            i.class1_att=att
            i.save()
        elif i.class2==subject_id:
            i.class2_att=att
            i.save()
        elif i.class3==subject_id:
            i.class3_att=att
            i.save()
        elif i.class4==subject_id:
            i.class4_att=att
            i.save()
        elif i.class5==subject_id:
            i.class5_att=att
            i.save()
        elif i.class6==subject_id:
            i.class6_att=att
            i.save()
        elif i.class7==subject_id:
            i.class7_att=att
            i.save()
        elif i.class8==subject_id:
            i.class8_att=att
            i.save()

        return redirect(f'/teacherdas/?subject_id={subject_id}')

    details=request.GET.get('details')
    subject_id=details[0:6]
    student_id=details[6:]

    sub=Subject.objects.filter(subject_id=subject_id)[0]
    date=sub.class_info.split(',')
    if len(date)!=0:
        date.pop(0)

    i=Student.objects.filter(student_id=student_id)[0]
    if i.class1==subject_id:
            att_str=i.class1_att
            att_list=list(att_str)
    elif i.class2==subject_id:
            att_str=i.class2_att
            att_list=list(att_str)
    elif i.class3==subject_id:
            att_str=i.class3_att
            att_list=list(att_str)
    elif i.class4==subject_id:
            att_str=i.class4_att
            att_list=list(att_str)
    elif i.class5==subject_id:
            att_str=i.class5_att
            att_list=list(att_str)
    elif i.class6==subject_id:
            att_str=i.class6_att
            att_list=list(att_str)
    elif i.class7==subject_id:
            att_str=i.class7_att
            att_list=list(att_str)
    elif i.class8==subject_id:
            att_str=i.class8_att
            att_list=list(att_str)
    date_att_list=[]
    for i in range(len(att_list)):
        z=[date[i],att_list[i],str(i)]
        date_att_list.append(z)

    dic={'date_att_list':date_att_list,'student_id':student_id , 'subject_id':subject_id}
    print(date_att_list)

    return render(request, 'editattendance.html',dic)
    
def editattendanceforadmin(request):
    if request.method == 'POST':
        details=request.GET.get('details')
        subject_id=details[0:6]
        student_id=details[6:]
        sub=Subject.objects.filter(subject_id=subject_id)[0]
        date=sub.class_info.split(',')
        if len(date)!=0:
            date.pop(0)

        att=''
        for j in range(len(date)):
            value=request.POST.get(str(j))
            print(value)
            att+=value
        
        i=Student.objects.filter(student_id=student_id)[0]
            
        if i.class1==subject_id:
            i.class1_att=att
            i.save()
        elif i.class2==subject_id:
            i.class2_att=att
            i.save()
        elif i.class3==subject_id:
            i.class3_att=att
            i.save()
        elif i.class4==subject_id:
            i.class4_att=att
            i.save()
        elif i.class5==subject_id:
            i.class5_att=att
            i.save()
        elif i.class6==subject_id:
            i.class6_att=att
            i.save()
        elif i.class7==subject_id:
            i.class7_att=att
            i.save()
        elif i.class8==subject_id:
            i.class8_att=att
            i.save()

        return redirect(f'/class_mgmt/?subject_id={subject_id}')

    details=request.GET.get('details')
    subject_id=details[0:6]
    student_id=details[6:]

    sub=Subject.objects.filter(subject_id=subject_id)[0]
    date=sub.class_info.split(',')
    if len(date)!=0:
        date.pop(0)

    i=Student.objects.filter(student_id=student_id)[0]
    if i.class1==subject_id:
            att_str=i.class1_att
            att_list=list(att_str)
    elif i.class2==subject_id:
            att_str=i.class2_att
            att_list=list(att_str)
    elif i.class3==subject_id:
            att_str=i.class3_att
            att_list=list(att_str)
    elif i.class4==subject_id:
            att_str=i.class4_att
            att_list=list(att_str)
    elif i.class5==subject_id:
            att_str=i.class5_att
            att_list=list(att_str)
    elif i.class6==subject_id:
            att_str=i.class6_att
            att_list=list(att_str)
    elif i.class7==subject_id:
            att_str=i.class7_att
            att_list=list(att_str)
    elif i.class8==subject_id:
            att_str=i.class8_att
            att_list=list(att_str)
    date_att_list=[]
    for i in range(len(att_list)):
        z=[date[i],att_list[i],str(i)]
        date_att_list.append(z)

    dic={'date_att_list':date_att_list,'student_id':student_id , 'subject_id':subject_id}
    print(date_att_list)

    return render(request, 'editattendanceforadmin.html',dic) 