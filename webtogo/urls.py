from django.contrib import admin
from django.urls import path
from . import views

app_name = "webtogo"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.service, name="service"),
    path("industries", views.industries, name="industries"),
    path("contactez-nous", views.contact, name="contact"),
    path("career", views.career, name="career"),
]