from django.shortcuts import render
from django.http import HttpResponse
from .models import entry
# Create your views here.
def index(request):
    return HttpResponse(entry.objects.all())

def addEntry(request, userEntry):
    #clean = cleaner(user_entry)
    itemizedEntry = userEntry.split(',')
    entrant = entry.objects.create(item = itemizedEntry[0], count = itemizedEntry[1], author = itemizedEntry[2])
    return HttpResponse(userEntry)