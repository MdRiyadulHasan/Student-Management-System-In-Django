# Generated by Django 4.2.4 on 2023-08-07 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('textId', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('firstName', models.CharField(max_length=150)),
                ('lastName', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=150, null=True, unique=True)),
                ('phone', models.CharField(max_length=30, unique=True)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(choices=[('BD', 'Bangladesh'), ('IND', 'India'), ('PAK', 'Pakistan'), ('US', 'United States'), ('QTR', 'Qatar')], default='BD', max_length=20)),
                ('password', models.CharField(max_length=150)),
                ('otpCode', models.CharField(blank=True, max_length=6, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'EndUser',
            },
        ),
        migrations.CreateModel(
            name='AdminHod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'Admin_Info',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'attendance_info',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(blank=True, max_length=255, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'department_info',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images1/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'teacher_info',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.department')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.teacher')),
            ],
            options={
                'db_table': 'subject_info',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('session_start_year', models.DateField()),
                ('session_end_year', models.DateField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.department')),
            ],
            options={
                'db_table': 'student_Info',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='NotificationTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.teacher')),
            ],
            options={
                'db_table': 'notification_teacher',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='NotificationStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.studentinfo')),
            ],
            options={
                'db_table': 'notification_student',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='LeaveReportTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_date', models.DateField()),
                ('leave_message', models.TextField(blank=True, null=True)),
                ('leave_status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.teacher')),
            ],
            options={
                'db_table': 'leaveReport_teacher',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='LeaveReportStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_date', models.DateField()),
                ('leave_message', models.TextField(blank=True, null=True)),
                ('leave_status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.studentinfo')),
            ],
            options={
                'db_table': 'leaveReport_student',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='FeedbackTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.studentinfo')),
            ],
            options={
                'db_table': 'feedback_teacher',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='FeedbackStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.studentinfo')),
            ],
            options={
                'db_table': 'feedback_student',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('attendance_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.attendance')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.studentinfo')),
            ],
            options={
                'db_table': 'attendance_report',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='attendance',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.subject'),
        ),
    ]
