# course/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.course_list, name='list')
]
