# Generated by Django 3.2.4 on 2021-10-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20211015_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
