from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('main/', views.main, name='main'), 
    path('contact/', views.contact, name='contact'), 
    path('base/', views.base, name='base')
]