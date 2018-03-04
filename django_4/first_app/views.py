from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def some(request):
    my_dir = {'name':'nitin','new' : 3}
    return render(request,'first_app/others.html',context=my_dir)
