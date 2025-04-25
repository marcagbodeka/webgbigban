from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index(request):
    return render(request, "webtogo/index.html")

def about(request):
    return render(request, "webtogo/about.html")

def service(request):
    return render(request, "webtogo/service.html")

def contact(request):
    return render(request, "webtogo/contact.html")

def industries(request):
    return render(request, "webtogo/industries.html")

def career(request):
    return render(request, "webtogo/career/career-1.html")