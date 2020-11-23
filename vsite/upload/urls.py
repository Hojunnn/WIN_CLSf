from django.urls import path
from .views import my_view

urlpatterns = [
    path('upload/', my_view, name='my-view')
]
