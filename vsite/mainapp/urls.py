from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.get, name='home'),
    path('category/', views.get , name='category'),
    url(r'^download/(?P<area>.+)/$', views.new,name='new'),
]
