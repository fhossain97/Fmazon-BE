# Generated by Django 4.1.4 on 2022-12-23 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='review',
        ),
    ]
