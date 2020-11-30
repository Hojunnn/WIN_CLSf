from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.get, name='home'),
    url(r'^category/(?P<area2>.+)/$', views.new2, name='category'),
    url(r'^download/(?P<area>.+)/$', views.new,name='new'),
]
