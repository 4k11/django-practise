from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,Webpage,AccessRecord,User
# Create your views here.


def index(request):
    webpagelist = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpagelist}
    return render(request,'firstapp/index.html',context=date_dict)
    

def help(request):
    help_dict = {'help_insert':"HELP PAGE"}
    return render(request,'secondapp/index.html',context=help_dict)


def user(request):
    user_list = User.objects.order_by('firstname')
    user_dict = {'user':user_list}
    return render(request,'firstapp/users.html',context=user_dict)