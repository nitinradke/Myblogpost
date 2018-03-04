from django.shortcuts import render
from first_app.forms import NewUserForm
from first_app.models import info_table

# Create your views here.
def index(request):
    acc_list = info_table.objects.order_by('rollno')
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
    my_dir = {'info_table' : acc_list,'form':form }
    return render(request,'first_app/index.html',context = my_dir)




def formpage(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request,'first_app/formpage.html',context = {'form':form})
