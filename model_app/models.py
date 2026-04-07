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

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    msg = models.TextField(verbose_name="Сообщение")
    dt = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время")
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True, verbose_name="Файл (фото/видео)")

    class Meta:
        ordering = ['-dt']  # сортировка по убыванию даты (новые сверху)

    def str(self):
        return f"{self.user.username}: {self.msg[:30]}"


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["msg"]


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]




