from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from first_app.models import Student,School
from django.urls import reverse_lazy
# Create your views here.


class Homepage(TemplateView):
    template_name = 'first_app/base.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "nitin"
        return context


class SchoolListView(ListView):
    model = School


class SchoolDetailView(DetailView):
    model = School
    template_name = 'first_app/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = School

class SchoolUpdateView(UpdateView):
    model = School
    fields = ("name","principal")


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('first_app:list')
