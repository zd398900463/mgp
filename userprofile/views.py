from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, logout, login
from .models import Profile
from .forms import CustomizeEdit, CustomizeLogin, CustomizeRegister
#装饰器，判断是否登录
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_page(request):
    # 若登录状态则直接进入主页
    if request.user.is_authenticated:
        return render(request, 'datastore/npolist.html')
    else:
        return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        user_login_form = CustomizeLogin(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect('datamanager:npolist')
            else:
                return render(request, "userprofile/login.html", {'错误': '用户名或密码错误！'})
        else:
            return render(request, "userprofile/login.html", {'错误': '用户名或密码错误！'})
    else:
        user_login_form = CustomizeLogin()
    context = {'user_login_form': user_login_form, 'user': request.user}
    return render(request, 'userprofile/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('userprofile:home')


def user_register(request):
    if request.method == "POST":
        user_register_form = CustomizeRegister(request.POST)
        if user_register_form.is_valid():
            user_register_form.save()
            user = authenticate(username=user_register_form.cleaned_data['username'],
                                password=user_register_form.cleaned_data['password1'])
            user.email = user_register_form.cleaned_data['email']
            Profile(user=user, realname=user_register_form.cleaned_data['realname'],
                    phone=user_register_form.cleaned_data['phone']).save()
            login(request, user)
            return redirect('datamanager:npolist')
    else:
        user_register_form = CustomizeRegister()
    context = {'user_register_form': user_register_form}
    return render(request, 'userprofile/register.html', context)


@login_required(login_url='userprofile:userlogin')
def user_edit(request):
    if request.method == "POST":
        user_edit_form = CustomizeEdit(request.POST, instance=request.user)
        if user_edit_form.is_valid():  # 判断表单是否符合要求（内容是否符合要求，是返回1，否返回0）
            user_edit_form.save()
            # print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',request.user.profile.realname)
            request.user.profile.realname = user_edit_form.cleaned_data['realname']
            request.user.profile.phone = user_edit_form.cleaned_data['phone']
            request.user.profile.save()
            return redirect("userprofile:useredit")
    else:
        user_edit_form = CustomizeEdit(instance=request.user)

    content = {'user_edit_form': user_edit_form, 'user': request.user}
    return render(request, 'userprofile/edit.html', content)


@login_required(login_url='userprofile:userlogin')
def password_change(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(data=request.POST,user=request.user)
        if password_change_form.is_valid():
            password_change_form.save()
            return redirect('userprofile:userlogin')
    else:
        password_change_form = PasswordChangeForm(user=request.user)
    content = {'password_change_form': password_change_form, 'user':request.user}
    return render(request, 'userprofile/pwdchange.html', content)
