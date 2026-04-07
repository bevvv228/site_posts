from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name

class Message(models.Model):
    msg = models.TextField(max_length=200)
    dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["msg"]


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]




