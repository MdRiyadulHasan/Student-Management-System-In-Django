# Generated by Django 4.2.4 on 2023-08-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='designamtion',
            field=models.CharField(choices=[('Lecturer', 'Lecturer'), ('Ast. Professor', 'Ast. Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor')], default='Lecturer', max_length=255),
        ),
    ]
