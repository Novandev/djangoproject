from django.shortcuts import render

# for repsponses
from django.http import HttpResponse
# Create your views here.

# Home route
def index(request):
    return HttpResponse('<h1>Testing that posts work</h1>')
