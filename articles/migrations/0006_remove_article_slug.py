# Generated by Django 3.0.3 on 2020-04-20 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20200329_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
