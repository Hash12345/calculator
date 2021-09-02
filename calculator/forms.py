from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput
from .models import Calculator
class CalculatorForm(forms.ModelForm):
    class Meta:
        model=Calculator
        fields="__all__"
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'first_name','last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control form-control-sm', 'placeholder':'Nick Name'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control form-control-sm', 'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control form-control-sm', 'placeholder':'Last Name'})
        self.fields['password1'].widget.attrs.update({'class':'form-control form-control-sm', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control form-control-sm', 'placeholder':'Confirm Password'})
class UpdateUserForm(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'password']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Last Name'}),
            'password':forms.PasswordInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Password'}),
        }