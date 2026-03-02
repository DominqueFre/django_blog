from . import views
from django.urls import path

urlpatterns = [
    path('', views.AboutList.as_view(), name='about_info'),
    # path('collaborate/', views.collaborate, name='collaborate'),
]
