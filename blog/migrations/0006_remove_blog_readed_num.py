# Generated by Django 2.0 on 2018-11-20 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_readnum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='readed_num',
        ),
    ]
