from django.urls import include, path
from django.shortcuts import render
from voyager.views import view, Settings, WordCardView
from . import views

app_name='voyager'
urlpatterns=[
    path('',views.view, name='home'),#name={namespace}
    path('history/',WordCardView.as_view(),name='archive'),
    path('<str:username>/', Settings.as_view(),name='user_settings'),
    
]
#namespace url format: {% url {app_name}:{namespace} {**context_obj} %}