from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new , name='new'),
]