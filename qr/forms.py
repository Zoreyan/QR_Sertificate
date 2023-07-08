from django import forms
from .models import *

class SertificateForm(forms.ModelForm):
    class Meta:
        model = Sertificate
        fields = ['name', 'settings']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name'
            }),
        }
    

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['template', 'x', 'y', 'title', 'font_size']

        widgets = {
            'template': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'template'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'title',
                'type': 'text'
            }),
            'x': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'x',
                'type': 'number'
            }),
            'y': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'x',
                'type': 'number'
            }),
            'font_size': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'font_size',
                'type': 'number'
            }),
        }