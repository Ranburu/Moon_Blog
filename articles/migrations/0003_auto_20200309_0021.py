# Generated by Django 3.0.3 on 2020-03-08 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_tumb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tumb',
            new_name='thumb',
        ),
    ]