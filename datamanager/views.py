from django.shortcuts import render
from .models import DataShow, DataSource
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from pyecharts.charts.bar import Bar
# Create your views here.


@login_required(login_url='userprofile:userlogin')
def npolist(request):
    body = DataShow.objects.all()
    context = {
        'titles': body
    }
    return render(request, 'datastore/npolist.html', context)


@login_required(login_url='userprofile:userlogin')
def npochart(request):
    return render(request, 'datastore/npochart.html')


@login_required(login_url='userprofile:userlogin')
def sentimentanalyse(request):
    return render(request, 'datastore/contentanalysis/npoas.html')


@login_required(login_url='userprofile:userlogin')
def intendanalyse(request):
    return render(request, 'datastore/contentanalysis/npois.html')


@login_required(login_url='userprofile:userlogin')
def datasorgin(request):
    return render(request, 'datastore/contentanalysis/dataorgin.html')


@login_required(login_url='userprofile:userlogin')
def hotpoint(request):
    return render(request, 'datastore/contentanalysis/hotpoint.html')


@login_required(login_url='userprofile:userlogin')
def userclass(request):
    return render(request, 'datastore/mediaanalysis/userclass.html')


@login_required(login_url='userprofile:userlogin')
def usergender(request):
    return render(request, 'datastore/mediaanalysis/usergender.html')

@login_required(login_url='userprofile:userlogin')
def weibosentiment(request):
    return render(request, 'datastore/mediaanalysis/weibosentiment.html')


@login_required(login_url='userprofile:userlogin')
def paidposters(request):
    return render(request, 'datastore/mediaanalysis/paidposters.html')


@login_required(login_url='userprofile:userlogin')
def transport(request):
    return render(request, 'datastore/mediaanalysis/transportroad.html')


@login_required(login_url='userprofile:userlogin')
def npomap(request):
    return render(request, 'datastore/mediaanalysis/npomap.html')


@login_required(login_url='userprofile:userlogin')
def statistics(request):
    return render(request, 'datastore/tools/statistics.html')


@login_required(login_url='userprofile:userlogin')
def sentiment(request):
    return render(request, 'datastore/tools/sentiment.html')

@login_required(login_url='userprofile:userlogin')
def abstract(request):
    return render(request, 'datastore/tools/abstract.html')

@login_required(login_url='userprofile:userlogin')
def keyword(request):
    return render(request, 'datastore/tools/keyword.html')

@login_required(login_url='userprofile:userlogin')
def themeclass(request):
    return render(request, 'datastore/tools/themeclass.html')

@login_required(login_url='userprofile:userlogin')
def dataconfig(request):
    return render(request, 'datastore/config.html')
