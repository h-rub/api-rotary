# Generated by Django 3.2.4 on 2021-06-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('_id_task', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
