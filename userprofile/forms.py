from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField


class CustomizeLogin(AuthenticationForm):
    verification = CaptchaField()


class CustomizeEdit(UserChangeForm):
    realname = forms.CharField(required=False, max_length=20)
    phone = forms.CharField(required=False, max_length=20)

    class Meta:
        model = User
        # 展示全部信息
        fields = ('username', 'password', 'email', 'realname', 'phone', ) #可以修改的内容

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #继承表单
        self.fields['username'].error_messages = {'unique': '用户名已存在！！！！！'}


class CustomizeRegister(UserCreationForm):
    realname = forms.CharField(required=False, max_length=20)
    phone = forms.CharField(required=False, max_length=20)
    verification = CaptchaField()

    class Meta:
        model = User
        # 展示全部信息
        fields = ('username', 'password1', 'password2', 'email', 'realname', 'phone', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #继承表单
        self.fields['username'].error_messages = {'unique': '用户名已存在！！！！！'}