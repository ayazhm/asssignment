from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import ModelForm, TextInput, EmailInput, NumberInput

class typeForm(ModelForm):
    class Meta:
        model = Diseasetype
        fields = ('id', 'description')

        widgets = {
            'id': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'ID'
            }),
            'description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Description'
            })
        }

class diseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = ('disease_code', 'pathogen', 'description', 'id')

        widgets = {
            'disease_code': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Disease code'
            }),
            'pathogen': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'pathogen'
            }),
            'description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Description'
            }),
            'id': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'ID'
            })
        }

class countryForm(ModelForm):
    class Meta:
        model = Country
        fields = ('cname', 'population')

        widgets = {
            'cname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
            }),
            'population': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
            })
        }

class userForm(ModelForm):
    class Meta:
        model = Users
        fields = ('email', 'name', 'surname', 'salary' ,'phone', 'cname')

        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
            }),
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
            }),
            'surname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
            }),
            'salary': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
            }),
            'phone': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
            }),
            'cname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 600px;',
            })
        }

