from django.conf.urls import url
from firstapp import views


urlpatterns = [
            url(r'^$',views.new,name='new'),
            url(r'^help/',views.help,name='help')
]
