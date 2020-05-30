"""apps1 URL Configuration
"""
from django.urls import path
from django.conf.urls import include, url
from . import views
from  rest_framework import routers

urlpatterns = [
    url(r'index', views.index, name='index')
]
