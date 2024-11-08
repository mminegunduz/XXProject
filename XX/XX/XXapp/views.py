from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
#from tweetapp.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.

def anasayfa(request):

    all_tivits= models.Tweet.objects.all()    # bütün gönderileri al
    tivit_sozluk= {"Gonderi": all_tivits}
    return render(request,'XXapp/anasayfa.html',context=tivit_sozluk) #bütün gönderileri getirdi

def gonderiekle(request):
    return render(request,'XXapp/gonderiekle.html')

def giris(request):
    return render(request,'XXapp/giris.html')

def hakkinda(request):
    return render(request,'XXapp/hakkinda.html')
