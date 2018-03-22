from django import forms
from django.contrib.auth import  authenticate

from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user=authenticate(username=username,password=password)

        if not user:
            raise forms.ValidationError(' this user does not exists ')

        if not user.check_password(password):
            raise forms.ValidationError('password is incorrect')

        return super(UserLoginForm,self).clean(*args,*kwargs)



class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')


    def clean_confirm(self):
        password1=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('confirm')

        if password1!=password2:
            raise forms.ValidationError(" Passwords don't match ")

        return password2



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password',
            'confirm',
        ]

    def clean_confirm(self):
        password1=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('confirm')

        if password1!=password2:
            raise forms.ValidationError(" Passwords don't match ")

        return password2
