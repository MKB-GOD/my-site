from django.shortcuts import render
from django.http import HttpResponse

def home_page(requests):
    return HttpResponse("<h1>homePage</h1>")

def contact_page(requests):
    return HttpResponse("<h1>contactPage</h1>")

def about_page(requests):
    return HttpResponse("<h1>aboutPage</h1>")
