from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_app, name="main_app"),
]