from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me':"I AM fromm views!"}
    return render(request,'firstapp/index.html',context=my_dict)
    

def help(request):
    help_dict = {'help_insert':"HELP PAGE"}
    return render(request,'secondapp/index.html',context=help_dict)


