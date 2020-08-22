from django.db import models
from django.contrib.auth.models import User

# from django.db.models import Model

# Create your models here
# class Contact(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=20)
#     notes = models.TextField()
#     time = models.DateTimeField()

#     def __str__(self):
#         return self.name


class Writeblog(models.Model):
    author = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    blogtopic = models.CharField(max_length=50)
    summary = models.TextField()
    avatar = models.ImageField(upload_to="media/", blank=True)
    blogpost = models.TextField()
    readtime = models.CharField(max_length=50)
    submitdate = models.DateTimeField()

    def __str__(self):
        return self.author


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    notes = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.name
