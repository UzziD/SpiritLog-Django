from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("The item collection goes here")
def addEntry(request):
    return HttpResponse(str(request))