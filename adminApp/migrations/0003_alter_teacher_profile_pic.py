# Generated by Django 4.2.4 on 2023-08-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_teacher_designamtion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]