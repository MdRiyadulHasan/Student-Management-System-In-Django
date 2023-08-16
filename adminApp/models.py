from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=255)
    faculty_name    = models.CharField(max_length=255)
    numberOfTeacher = models.IntegerField()
    numberOfStudent = models.IntegerField()
    estblished      = models.CharField(max_length=255)

    class Meta:
        db_table = 'department'
    def __str__(self):
        return self.department_name

class Teacher(models.Model):
    teacherName       = models.CharField(max_length=250)
    department        = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    email             = models.EmailField(max_length=255)
    phone             = models.CharField(max_length=255)
    password          = models.CharField(max_length=255)
    gender            = models.CharField(max_length=255)
    address           = models.CharField(max_length=255, blank=True, null=True)
    profile_pic       = models.ImageField(upload_to='TeacherImage/', blank=True, null=True) 
    created           = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated           = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'teacher_info'
        ordering = ['-created']
        
    def __str__(self):
        return self.teacherName
    
class Course(models.Model):
    courseName      = models.CharField(max_length=255)
    courseId        = models.CharField(max_length=255)
    credit          = models.CharField(max_length=255)
    department      = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    teacher         = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    created         = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'course_info'
        ordering = ['-created']
        
    def __str__(self):
        return self.courseName