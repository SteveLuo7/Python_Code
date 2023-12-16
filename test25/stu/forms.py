from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=8)
    password = forms.CharField(max_length=3,widget=forms.PasswordInput)