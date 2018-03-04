from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dir = {'insert_me':"Hello from views.py"}
    return render(request,'firstapp/index.html',context=my_dir)
def new(request):
    return HttpResponse("hello to url")

def help(request):
    my_dir = {'get_help':"THis is from views.py"}
    return render(request,'firstapp/help.html',context=my_dir)
