from django.shortcuts import render
from learning_users.forms import UserForm,UserProfileInfoForm
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request,'learning_users/base.html')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('learning_users:base'))



def register(request):
    user = UserForm()
    profile = UserProfileInfoForm()
    if request.method == "POST":
        user = UserForm(request.POST)
        profile = UserProfileInfoForm(request.POST)
        if user.is_valid() and profile.is_valid():
            still_not_done = user.save()
            still_not_done.set_password(still_not_done.password)
            still_not_done.save()
            profile_temp = profile.save(commit = False)
            profile_temp.user = still_not_done


            if 'profile_pic' in request.FILES:
                print("gatta you!")
                profile_temp.profile_pic = request.FILES['profile_pic']

            profile_temp.save()

    return render(request,'learning_users/registration.html',
                                  context = {'user_form':user,
                                   'profile_form':profile})





def user_login(request):
    hack = False
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:

                login(request,user)

                return HttpResponseRedirect(reverse('learning_users:base'))
            else:
                return HttpResponse("Your account is suspended contact at nitinradke@gmail.com")
        else:
            hack = True
            return render(request,'learning_users/login.html')
    else:
        return render(request,'learning_users/login.html',{'hack':hack})
