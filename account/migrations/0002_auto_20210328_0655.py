# Generated by Django 3.1.7 on 2021-03-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='personal_number',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Manager', 'Manager')], max_length=10),
        ),
    ]
