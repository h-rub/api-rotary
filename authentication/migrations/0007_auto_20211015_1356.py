# Generated by Django 3.2.4 on 2021-10-15 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20211015_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
    ]