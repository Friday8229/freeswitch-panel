from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ApiReq, name="home"),
    path('temp/', views.home, name="temp"),
    path('api_req/', views.ApiReq, name="api_req"),
    path('api_conf/', views.mod_conf, name="api_conf"),
    path('api_activeCalls/', views.active_calls, name="active_calls"),
]

