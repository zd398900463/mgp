from django.urls import path
from . import views

app_name = 'datamanager'
urlpatterns = [
    path('npolist/', views.npolist, name='npolist'),
    path('npochart/', views.npochart, name='npochart'),
    path('nposa/', views.sentimentanalyse, name='nposa'),
    path('npoia/', views.intendanalyse, name='npoia'),
    path('orgin/', views.datasorgin, name='orgin'),
    path('hotpoint/', views.hotpoint, name='hotpoint'),
    path('usergender/', views.usergender, name='gender'),
    path('userclass/', views.userclass, name='class'),
    path('weibosentiment/', views.weibosentiment, name='weibosentiment'),
    path('paidposters/', views.paidposters, name='paidposters'),
    path('transport/', views.transport, name='transport'),
    path('npomap/', views.npomap, name='npomap'),
    path('statistics/', views.statistics, name='statistics'),
    path('abstract/', views.abstract, name='abstract'),
    path('keyword/', views.keyword, name='keyword'),
    path('themeclass/', views.themeclass, name='themeclass'),
    path('sentiment/', views.sentiment, name='sentiment'),
    path('dataconfig/', views.dataconfig, name='config'),
]