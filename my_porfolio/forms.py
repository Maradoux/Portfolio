from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta: 
        model = Message
        fields = ['full_name', 'email', 'subject', 'message']
    