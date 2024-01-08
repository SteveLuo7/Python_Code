from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=30,
                               widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username/Email'}))
    password = forms.CharField(label='密码', min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username == password:
            raise forms.ValidationError('用户名与密码不能相同')
        return password


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email', max_length=30, widget=forms.EmailInput(attrs={'class': 'input',
                                                                                           'placeholder': 'Email'}))
    password = forms.CharField(label='密码', min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))

    password1 = forms.CharField(label='再次输入密码', min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError("Email has already been used")
        return email

    def clean_password1(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("TWICE PASSWORD YOU INPUT IS NOT SAME")
        return self.cleaned_data['password1']


class ForgetPwdForm(forms.Form):
    '''填写Email表单页面'''
    email = forms.EmailField(label="请输入注册邮箱地址", min_length=4, widget=forms.EmailInput(attrs={'class':'input','placeholder':'用户名/邮箱'}))

class ModifyPwdForm(forms.Form):
    '''修改密码表单'''
    password = forms.CharField(label="输入新密码",
                               min_length=6,
                               widget=forms.PasswordInput(attrs={'class':'input',
                                                                 'placeholder':'输入密码'}))