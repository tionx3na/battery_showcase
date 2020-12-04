from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_app, name="main_app"),
    path('shop', views.showcase, name="showcase"),
    path('details', views.details, name="details"),
    path('contact', views.contacts, name="contact"),
]