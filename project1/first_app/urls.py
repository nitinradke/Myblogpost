from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
                path('table/',views.index,name = 'index'),
                path('',views.user_login,name='login'),
                path('logout/',views.user_logout,name = 'logout'),
]
