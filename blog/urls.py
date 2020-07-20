from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index)
    , path('post_login', views.post_login, name='post_login')
    , path('post_register', views.post_register, name='post_register')
    ,
]
