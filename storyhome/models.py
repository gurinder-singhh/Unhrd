from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True) # default = timezone.now
    # delete the post if user is deleted
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    view = models.IntegerField(null=True,blank=True)
    likes = models.IntegerField(null=True,blank=True)
    tags = models.TextField(default=None)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Friends(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User,null=True,related_name='friends_of',on_delete=models.CASCADE)



