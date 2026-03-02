from . import views
from django.urls import path

urlpatterns = [
    path('', views.collaborate_request, name='about_info'),
    # path('', views.collaborate_request, name='collaborate_request'),
]
