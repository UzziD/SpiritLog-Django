from django.urls import __path__
from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addEntry/', views.addEntry, name='addEntry')

]