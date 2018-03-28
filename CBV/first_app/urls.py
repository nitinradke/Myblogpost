from django.urls import path
from first_app import views

app_name = 'first_app'
urlpatterns =[
    #path('',views.CBVs.as_view()),
    path('',views.templateview.as_view(),name = "index"),
    path('list/',views.School_list.as_view(),name = "school_list"),
    path('register/',views.Register_school.as_view(),name = "school_form"),
    path('update/<pk>\d+',views.Update_View.as_view(),name = "school_update"),

]
