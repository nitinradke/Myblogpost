from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,CreateView,UpdateView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# Create your views here.



class templateview(TemplateView):
    template_name = 'index.html'


class School_list(ListView):
    model = models.School
    # template_name = "school_list.html"

class Register_school(CreateView):
    fields = ("name","age","city")
    model = models.School
    success_url = reverse_lazy("first_app:index")

class Update_View(UpdateView):
    fields = ("name,age")
    model = models.School
