# Generated by Django 3.2.4 on 2021-10-11 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_is_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_complete',
            new_name='is_completed',
        ),
    ]
