from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('main', views.main_app, name="main_app"),
    path('shop', views.showcase, name="showcase"),
    path('details/<str:range_name>+range', views.details, name="details"),
    path('details/search/<str:range_name>+range', views.search, name="search"),
    path('details/search/models/<str:model_name>+range', views.models, name="models"),
    path('details/search/models/search/<str:range_name>+range', views.search, name="models"),
    path('contact', views.contacts, name="contact"),
    path('models', views.models, name="models"),
    path('shop2', views.amaron, name="amaron"),
    path('about', views.about, name="about"),
]