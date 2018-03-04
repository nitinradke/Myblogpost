from django.conf.urls import url
from . import views
urlpatterns = [
            url(r'^index',views.information),
            url(r'^form',views.formpage)

]
