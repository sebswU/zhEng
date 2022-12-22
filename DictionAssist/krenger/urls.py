from django.urls import include, path
from django.shortcuts import render
from krenger.views import Form, Settings, WordArchive
from . import views

app_name='krenger'
urlpatterns=[
    path('home/',Form.as_view(), name='home'),
    path('<str:username>/', Settings.as_view(),name='user_settings'),
    path('history/',WordArchive.as_view(),name='archive'),
]