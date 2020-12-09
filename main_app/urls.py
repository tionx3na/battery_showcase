from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name="landing"), #landing page
    path('main', views.main_app, name="main_app"),  # Main page of BOSCH
    path('shop', views.showcase, name="showcase"),  # BOsch series showcase
    path('details/<str:range>+range', views.details, name="details"),  # Bosch series Details
    path('details/search/<str:range>+range<str:range_name>+range', views.search, name="search"),  # Bosch Search
    path('details/search/models/<str:model_name>+range', views.models, name="models"),  # Bosch model details
    path('contact', views.contacts, name="contact"),  # Contact page
    path('models', views.models, name="models"),  # Amaron models page
    path('shop2', views.amaron, name="amaron"),  # Amaron main page
    path('about', views.about, name="about"),  # About page
    path('search2/<str:name>+range',views.search2, name="search2"), # Amaron search page
    path('search2/adetails/<str:amodel>+range', views.amarondetails, name="adetails"), # Amaron details view page
]