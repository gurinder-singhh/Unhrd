# Generated by Django 3.0.8 on 2020-07-19 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storyhome', '0007_remove_friends_current_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='friends',
            new_name='users',
        ),
    ]
