from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['msg', 'attachment']
        widgets = {
            'msg': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Напишите сообщение...'}),
            'attachment': forms.ClearableFileInput(attrs={'accept': 'image/*,video/*'}),
        }