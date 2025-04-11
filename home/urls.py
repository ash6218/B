from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.say_hello, name='home'),
    path('', views.home, name='first_form'),
    path('detail/<int:todo_id>/', views.detail, name = 'detail'),
]
