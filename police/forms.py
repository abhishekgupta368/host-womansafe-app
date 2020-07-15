from django import forms
from django.forms import ModelForm
from .models import Police
from .models import Location

class PoliceSignInForm(ModelForm):
    class Meta:
        model = Police
        fields = '__all__'
        widgets = {
                'password': forms.PasswordInput,
            }