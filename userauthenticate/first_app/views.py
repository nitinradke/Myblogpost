from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'first_app/index.html')



def register(request):
    # return HttpResponse("nitin radke")
    form = forms.UserForm()
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            form_save.set_password(form_save.password)
            form_save.save()
            return HttpResponseRedirect("index")

    return render(request,'first_app/register.html',{'form':form})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('first_app:index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'first_app/loginform.html', {})
