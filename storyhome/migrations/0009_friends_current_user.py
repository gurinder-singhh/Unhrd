# Generated by Django 3.0.8 on 2020-07-19 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storyhome', '0008_auto_20200719_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends_of', to=settings.AUTH_USER_MODEL),
        ),
    ]
