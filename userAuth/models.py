from re import template
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.conf import settings
from django.dispatch import receiver
from django.template.loader import render_to_string



# Create your models here.
class UserRegistration(User):
    confirm_password = models.CharField(max_length=60)
    #uuid = models.UUIDField(unique=True, blank=False, db_index = True)


    # def save(self):
    #     self.full_clean()
    #     super().__init__()

@receiver(post_save, sender=User)
def send_email(sender,**kwargs):
    template = 'userAuth/verifyemail.html'

    email = EmailMessage(
    'Hello',
    'Body goes here',
    settings.EMAIL_HOST_USER,
    ['igarrybachhal@gmail.com'],
    )
    email.fail_silently = False
    email.send()


