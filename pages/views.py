from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs): # *args, **kwargs
    return HttpResponse("<h1>Hello World</h1><h2>Subheader</h2>") # string of html code