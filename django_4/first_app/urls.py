from django.conf.urls import url
from first_app.views import index,some



app_name = 'nitin'

urlpatterns = [
        url(r'^index',index,name = 'index'),
        url(r'^other',some,name = 'other')

]
