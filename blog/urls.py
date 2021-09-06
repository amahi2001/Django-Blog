from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),

    #when someone inputs an int after the /blog/ the page will redirect to a new html page and display the object independently
    path('<int:blog_id>/', views.detail, name= 'detail'),
]
