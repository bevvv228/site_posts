from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name
def validate_file_size(value):
    limit = 10 * 1024 * 1024  # 10 МБ
    if value.size > limit:
        raise ValidationError('Файл слишком большой. Максимум 10 МБ.')
class Message(models.Model):
    msg = models.TextField(max_length=200)
    dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    media = models.FileField(
        upload_to='posts/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif', 'webp', 'mp4', 'webm', 'mov']),
            validate_file_size,
        ],
    )


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["msg", "media"]


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]




