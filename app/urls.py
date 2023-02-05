from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="index"),
    path("about",views.about, name="about"),
    path("blog_details",views.blog_details, name="blog_details"),
    path("blog",views.blog, name="blog"),
    path("contact",views.contact, name="contact"),
    path("doctors",views.doctors, name="doctors"),
    path("login",views.login, name="login"),
]

