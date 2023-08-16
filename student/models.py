from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import transaction
# End User Signup Model
 
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password."""
        if not email:
            raise ValueError("The given email must be set")
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password=password, **extra_fields)




class EndUser(AbstractBaseUser):
    textId               = models.CharField(max_length=150, unique = True, blank=True, null=True)
    firstName            = models.CharField(max_length=150)
    lastName             = models.CharField(max_length=150, blank=True, null=True)
    email                = models.EmailField(max_length=150, unique=True, blank=True, null=True)
    phone                = models.CharField(max_length=30, unique=True)
    city                 = models.CharField(max_length=100)
    country_data = (("BD", "Bangladesh"), ("IND", "India"), ("PAK","Pakistan"), ("US", "United States"), ("QTR","Qatar"))
    country              = models.CharField(max_length=20, choices=country_data, default="BD")
    password             = models.CharField(max_length=150)
    otpCode              = models.CharField(max_length=6, blank=True, null=True)
    created              = models.DateTimeField(auto_now_add=True)
    updated              = models.DateTimeField(auto_now=False, blank=True, null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]
   
    def __str__(self):
        return self.firstName
    
    class Meta:
        db_table = 'EndUser'

# Create your models here.


# class AdminHod(models.Model):
#     firstName  = models.CharField(max_length=255)
#     lastName   = models.CharField(max_length=255, blank=True, null=True)
#     email      = models.EmailField(max_length=255)
#     phone      = models.CharField(max_length=255)
#     password   = models.CharField(max_length=255)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)

#     class Meta:
#         db_table = 'Admin_Info'
#         ordering = ['-created']

#     def __str__(self):
#         return self.firstName  

    

    
# class StudentInfo(models.Model):
#     firstName  = models.CharField(max_length=255)
#     lastName   = models.CharField(max_length=255, blank=True, null=True)
#     email      = models.EmailField(max_length=255)
#     phone      = models.CharField(max_length=255)
#     password   = models.CharField(max_length=255)
#     gender     = models.CharField(max_length=255)
#     department  = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
#     session_start_year = models.DateField()
#     session_end_year = models.DateField()
#     address    = models.CharField(max_length=255, blank=True, null=True)
#     profile_pic = models.ImageField(upload_to='images/', blank=True, null=True) 
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)

#     class Meta:
#         db_table = 'student_Info'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.firstName+" "+self.lastName

# class Attendance (models.Model):
#     subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
#     attendance_date = models.DateTimeField(auto_now_add=True)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         db_table = 'attendance_info'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.subject_id
    
# class AttendanceReport(models.Model):
#     student_id = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
#     attendance_id = models.ForeignKey(Attendance, on_delete=models.DO_NOTHING)
#     status = models.BooleanField(default=False)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         db_table = 'attendance_report'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.student_id
    
# class LeaveReportStudent(models.Model):
#     student_id = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
#     leave_date = models.DateField()
#     leave_message  = models.TextField(blank=True, null=True)
#     leave_status = models.BooleanField(default=False)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         db_table = 'leaveReport_student'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.student_id

# class LeaveReportTeacher(models.Model):
#     teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
#     leave_date = models.DateField()
#     leave_message  = models.TextField(blank=True, null=True)
#     leave_status = models.BooleanField(default=False)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         db_table = 'leaveReport_teacher'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.teacher_id
    
# class FeedbackStudent(models.Model):
#     student_id = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
#     feedback = models.TextField()
#     feedback_reply  = models.TextField(blank=True, null=True)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         db_table = 'feedback_student'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.feedback
    
# class FeedbackTeacher(models.Model):
#     teacher_id = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
#     feedback = models.TextField()
#     feedback_reply  = models.TextField(blank=True, null=True)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         db_table = 'feedback_teacher'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.feedback
    
# class NotificationStudent(models.Model):
#     student_id = models.ForeignKey(StudentInfo, on_delete=models.DO_NOTHING)
#     message = models.TextField(blank=True, null=True)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         db_table = 'notification_student'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.feedback
    
# class NotificationTeacher(models.Model):
#     teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
#     message = models.TextField(blank=True, null=True)
#     created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
#     class Meta:
#         db_table = 'notification_teacher'
#         ordering = ['-created']
        
#     def __str__(self):
#         return self.feedback





