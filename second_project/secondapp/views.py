from django.shortcuts import render
from django.http import HttpResponse
from secondapp.models import Website,Topic,AccessRecord
# Create your views here.

def index(request):
    return HttpResponse("Hello this is a test")
def new(request):
    return HttpResponse("hello this is url forwarding")

def templates(request):
    my_dir = {'insert_me':'THis is comming from views.py'}
    return render(request,'secondapp/help.html',context = my_dir)
def info(request):
    my_list = AccessRecord.objects.order_by('date')
    my_dir = {'values':my_list}
    return render(request,'secondapp/list.html',context = my_dir)
