from django.urls import path, include
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('password_change/', views.password_change, name='pwdchange'),
    path('user_edit/', views.user_edit, name='useredit'),
    path('user_login/', views.user_login, name='userlogin'),
    path('user_logout/', views.user_logout, name='userlogout'),
    path('user_register/', views.user_register, name='userregister'),
]
