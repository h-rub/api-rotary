# Generated by Django 3.2.4 on 2021-11-05 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myclub', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]