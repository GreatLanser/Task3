from django.core.exceptions import ValidationError

from .models import Users
from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = Users
        fields = ('username', 'email', 'password', 'password2')

    field_order = ['username', 'email', 'password', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if Users.objects.filter(email__iexact=email).exists():
            raise ValidationError('The email already exist.',  code='invalid')
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']