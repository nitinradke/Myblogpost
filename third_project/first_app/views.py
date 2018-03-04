from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import info
from first_app.forms import NewUserForm
# Create your views here.
def index(request):
    return HttpResponse("Enter /list in url to view page")


def template_view(request):
    my_dir = {"values":"this is content"}
    return render(request,'first_app/list.html',context = my_dir)


def make_list(request):
    list_var = info.objects.order_by('First_name')
    my_dir = {'access_list':list_var}
    return render(request,'first_app/list.html',context =my_dir)


def myform(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)

    return render(request,'first_app/forms.html',context = {'form':form})
