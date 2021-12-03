from django import urls
from django.urls import path
from django.urls.conf import re_path
from django.urls.resolvers import URLPattern
from.import views

app_name = "FridgeApp"
urlpatterns = [
    # re_path(r'^$',views.FooDListing,name="FoodListing"),
    re_path(r'^$',views.RecettesListing,name="RecettesListing"),


] 