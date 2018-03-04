from django.urls import path,include
from learning_users import views

app_name = "learning_users"

urlpatterns = [
        path('base/',views.base,name = 'base'),
        path('register/',views.register,name='register'),
        path('login/',views.user_login,name='user_login'),
        path('logout/',views.user_login,name='user_logout'),

]
