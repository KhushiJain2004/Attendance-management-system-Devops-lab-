from django.db import models

class Subject(models.Model):
    subject_id=models.CharField(max_length=15)
    subject_name=models.CharField(max_length=30)
    # batch_id=models.CharField(max_length=15)
    teacher_id=models.CharField(max_length=15)
    classes_held=models.IntegerField()
    number_of_students=models.IntegerField()
    class_info=models.TextField()
    def __str__(self):
        return self.subject_id
    
class Teacher(models.Model):
    teacher_id=models.CharField(max_length=15)
    teacher_name=models.CharField(max_length=30)
    # batch_id=models.CharField(max_length=15)
    email_id=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.teacher_id
    
class Student(models.Model):
    student_id=models.CharField(max_length=15)
    student_name=models.CharField(max_length=30)
    # batch_id=models.CharField(max_length=15)
    email_id=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    class1=models.CharField(max_length=20,default='')
    class1_att=models.CharField(max_length=100,default='')
    class2=models.CharField(max_length=20,default='')
    class2_att=models.CharField(max_length=100,default='')
    class3=models.CharField(max_length=20,default='')
    class3_att=models.CharField(max_length=100,default='')
    class4=models.CharField(max_length=20,default='')
    class4_att=models.CharField(max_length=100,default='')
    class5=models.CharField(max_length=20,default='')
    class5_att=models.CharField(max_length=100,default='')
    class6=models.CharField(max_length=20,default='')
    class6_att=models.CharField(max_length=100,default='')
    class7=models.CharField(max_length=20,default='')
    class7_att=models.CharField(max_length=100,default='')
    class8=models.CharField(max_length=20,default='')
    class8_att=models.CharField(max_length=100,default='')
    def __str__(self):
        return self.student_id