from django.urls import path
from blog.views import *

app_name = "blog-for-travel"

urlpatterns = [
path("blog",main_blog,name="m_blog"),
path("s_blog",single_blog,name="s_blog")
]
