# Generated by Django 3.2.4 on 2021-10-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20211015_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimagetest',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
