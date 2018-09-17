# import both modules to sue them in this project
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Home route. To get the view this will be in the views folder with the function def index():
    url('^$', views.index, name='index')
]
