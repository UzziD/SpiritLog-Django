from django.shortcuts import render
from django.http import HttpResponse
from .models import entry
# Create your views here.
def index(request):
    allentries = entry.objects
    output = '\n'.join(allentries) #lists every entry in the collection
    return HttpResponse(output)
def addEntry(request, userEntry: str):
    #clean = cleaner(user_entry)
    itemizedEntry = userEntry.split(',')
    entrant = entry.objects.create(item = itemizedEntry[0], count = itemizedEntry[1], author = itemizedEntry[2])
    return HttpResponse(str(entrant))