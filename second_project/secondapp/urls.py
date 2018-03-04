from django.conf.urls import url
from secondapp import views

urlpatterns = [
                url(r'^$',views.new,name='new'),
                url(r'^templates',views.templates,name='template'),
                url(r'^list',views.info,name='info'),
]
