from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry
# Create your views here.
def index(request):
    return HttpResponse(Entry.objects.all())

def addEntry(request, userEntry):
    #clean = cleaner(user_entry)
    itemizedEntry = userEntry.split(',')
    entrant = Entry.objects.create(item = itemizedEntry[0], count = itemizedEntry[1], author = itemizedEntry[2])
    return HttpResponse(userEntry)