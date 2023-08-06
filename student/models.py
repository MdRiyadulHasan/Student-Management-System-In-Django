from django.db import models

# Create your models here.
class Admin(models.Model):
    firstName  = models.CharField(max_length=255)
    lastName   = models.CharField(max_length=255, blank=True, null=True)
    email      = models.EmailField(max_length=255)
    phone      = models.CharField(max_length=255)
    password   = models.CharField(max_length=255)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'Admin_Info'
        ordering = ['-created']

    def __str__(self):
        return self.firstName  

    
class Staff(models.Model):
    name  = models.CharField(max_length=255)
    email      = models.EmailField(max_length=255)
    phone      = models.CharField(max_length=255)
    password   = models.CharField(max_length=255)
    gender     = models.CharField(max_length=255)
    address    = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='images1/', blank=True, null=True) 
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'staff_info'
        ordering = ['-created']
        
    def __str__(self):
        return self.name
class Department(models.Model):
    department_name = models.CharField(max_length=255, blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'department_info'
        ordering = ['-created']
        
    def __str__(self):
        return self.department_name
    
class Subject(models.Model):
    subject_name  = models.CharField(max_length=255, blank=True, null=True)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    staff_id      = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    created       = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated       = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'subject_info'
        ordering = ['-created']
        
    def __str__(self):
        return self.subject_name
    
class Student(models.Model):
    firstName  = models.CharField(max_length=255)
    lastName   = models.CharField(max_length=255, blank=True, null=True)
    email      = models.EmailField(max_length=255)
    phone      = models.CharField(max_length=255)
    password   = models.CharField(max_length=255)
    gender     = models.CharField(max_length=255)
    department  = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    address    = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='images/', blank=True, null=True) 
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'student_Info'
        ordering = ['-created']
        
    def __str__(self):
        return self.firstName+" "+self.lastName

class Attendance (models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    attendance_date = models.DateTimeField(auto_now_add=True)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        db_table = 'attendance_info'
        ordering = ['-created']
        
    def __str__(self):
        return self.subject_id
    
class AttendanceReport(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        db_table = 'attendance_report'
        ordering = ['-created']
        
    def __str__(self):
        return self.student_id
    
class LeaveReportStudent(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    leave_date = models.DateField()
    leave_message  = models.TextField(blank=True, null=True)
    leave_status = models.BooleanField(default=False)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        db_table = 'leaveReport_student'
        ordering = ['-created']
        
    def __str__(self):
        return self.student_id

class LeaveReportStaff(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    leave_date = models.DateField()
    leave_message  = models.TextField(blank=True, null=True)
    leave_status = models.BooleanField(default=False)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        db_table = 'leaveReport_staff'
        ordering = ['-created']
        
    def __str__(self):
        return self.staff_id
    
class FeedbackStudent(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    feedback_reply  = models.TextField(blank=True, null=True)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        db_table = 'feedback_student'
        ordering = ['-created']
        
    def __str__(self):
        return self.feedback
    
class FeedbackStaff(models.Model):
    staff_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    feedback_reply  = models.TextField(blank=True, null=True)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        db_table = 'feedback_staff'
        ordering = ['-created']
        
    def __str__(self):
        return self.feedback
    
class NotificationStudent(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    message = models.TextField(blank=True, null=True)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        db_table = 'notification_student'
        ordering = ['-created']
        
    def __str__(self):
        return self.feedback
    
class NotificationStaff(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    message = models.TextField(blank=True, null=True)
    created    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated    = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        db_table = 'notification_staff'
        ordering = ['-created']
        
    def __str__(self):
        return self.feedback





