from django import urls
from django.urls import path
from django.urls.conf import re_path
from django.urls.resolvers import URLPattern
from.import views

app_name = "FridgeApp"
urlpatterns = [
    re_path(r'^$',views.FooDListing,name="FooDListing"),
    path(r'Recettes/',views.RecettesListing,name="RecettesListing"),
    path('HowToCook/',views.HowToCook,name="HowToCook"),
    path('search/',views.Search,name="search"),


] 