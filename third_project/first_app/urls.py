from django.conf.urls import url
from first_app import views
urlpatterns =[
        url(r'^$',views.index,name='index'),
        url(r'^list',views.make_list,name='template'),
        url(r'^form',views.myform,name='form')
]
