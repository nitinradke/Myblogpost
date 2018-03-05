from django.shortcuts import render
from first_app.forms import NewUserForm
from first_app.models import info_table
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.
@login_required
def index(request):
    acc_list = info_table.objects.order_by('rollno')
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
    my_dir = {'info_table' : acc_list,'form':form }
    return render(request,'first_app/index.html',context = my_dir)






def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("first_app:index"))
            else:
                return HttpResponse(" Your account is been suspended contact adminstrator")
        else:
            return HttpResponse("Incorrect username passowrd combination")
    return render(request,'first_app/login.html',{},RequestContext(request))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:login'))
