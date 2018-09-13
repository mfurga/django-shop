from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': _('Username')
        })
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': _('Your password')
        })
    )
    password_repeat = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': _('Repeat your password')
        })
    )
    terms = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).count():
            raise forms.ValidationError(_('This user already exists.'))
        return email

    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise forms.ValidationError(_('Passwords are not the same.'))
        return password_repeat


class SigninForm(forms.Form):
    username = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': _('Username')
        })
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': _('Your password')
        })
    )
