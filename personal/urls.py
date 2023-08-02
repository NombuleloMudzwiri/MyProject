# personal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('', views.about, name='about'),
]
