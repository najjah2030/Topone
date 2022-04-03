from email import message
from inspect import _SourceObjectType
from pydoc import describe
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description= models.CharField(max_length=150)

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    Board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_dt= models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)