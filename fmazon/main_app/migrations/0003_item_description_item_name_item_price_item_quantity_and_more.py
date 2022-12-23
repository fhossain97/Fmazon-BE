# Generated by Django 4.1.4 on 2022-12-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='No Description Found', max_length=500),
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.CharField(default='No Comment Yet!', max_length=300),
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
