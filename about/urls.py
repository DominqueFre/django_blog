from django.urls import path
from . import views


urlpatterns = [
    path('', views.collaborate, name='about_info'),
]
