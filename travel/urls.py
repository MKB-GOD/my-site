from django.urls import path
from travel.views import *

app_name = "Travel"

urlpatterns = [
    path('', home_page,name="home"),
    path('contact', contact_page,name="contact"),
    path('about', about_page,name="about"),
]
