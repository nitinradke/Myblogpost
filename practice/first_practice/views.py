from django.shortcuts import render
from first_practice.models import info
from first_practice.forms import basicform,NewUserForm
# Create your views here.
def index(request):
    return render(request,'index.html')


def information(request):
    obj = info.objects.order_by('name')
    my_dir = {'values': obj }
    return render(request,'index.html',context =my_dir)

def formpage(request):
    obj = NewUserForm()
    if request.method == 'POST':
        obj = NewUserForm(request.POST)
        if obj.is_valid():
            obj.save()
            return index(request)
        
    return render(request,'formpage.html',{'form':obj})
