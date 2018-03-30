from django.urls import path
from blog import views


urlpatterns = [
        path('',views.index.as_view(),name='index'),
]
