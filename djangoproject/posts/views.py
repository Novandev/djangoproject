from django.shortcuts import render

# for repsponses
from django.http import HttpResponse
# Create your views here.

# Home route
def index(request):
    return render(request, 'posts/index.html',{
    'title':'Novans Latest Posts'
    })
