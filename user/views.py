from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def loginView(response):
    return HttpResponse("Login page from dummy view")