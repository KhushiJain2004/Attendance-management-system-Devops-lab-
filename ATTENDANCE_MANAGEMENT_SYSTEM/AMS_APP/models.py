from django.db import models

class Subject(models.Model):
    subject_id=models.CharField(max_length=15)
    subject_name=models.CharField(max_length=30)
    # batch_id=models.CharField(max_length=15)
    teacher_id=models.CharField(max_length=15)
    classes_held=models.IntegerField()
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
    def __str__(self):
        return self.student_id