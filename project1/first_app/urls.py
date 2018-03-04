from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
                path('table/',views.index,name = 'index'),
                path('formpage/',views.formpage,name = 'formpage')
]
