# Generated by Django 3.0.8 on 2020-07-19 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storyhome', '0006_friends_current_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='current_user',
        ),
    ]
