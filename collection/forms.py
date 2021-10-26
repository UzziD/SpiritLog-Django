#import form class from django
from django import forms
from django.forms import fields

#import Entry model from models.py
from .models import Entry

#ModelForm for Entry
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = "__all__"