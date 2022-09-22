from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    logo = models.ImageField(max_length=400)
    
    def __str__(self):
        return self.user.username


class Photo(models.Model):
    image = models.ImageField(max_length=400)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = TaggableManager()


class Album(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photos = models.ManyToManyField(Photo)

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    content = models.TextField(blank=True)


class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
