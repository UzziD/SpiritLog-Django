from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from .models import Entry
from .models import RareDropTableItems
from .forms import EntryForm
from django.core import serializers
# Create your views here.

def index(request):
    allEntries = Entry.objects.all()
    #output = ', '.join([e.__str__() for e in allEntries])
    data = serializers.serialize("jsonl", Entry.objects.all())
    return HttpResponse(data,content_type="application/json")

def addEntry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            try:
                formItem = form['item'].value()
                item = RareDropTableItems.objects.get(itemAlias=formItem).item  #grab item name based on user's input item
                itemEntry = form.save(commit=False)                     #save the non validated form to change to proper item name
                itemEntry.item = item
                itemEntry.save()
                return HttpResponseRedirect('/collection/')
            except Exception as e:
                return HttpResponseBadRequest(str(form['item'].value()) + " returned error: {}".format(e))
    else:
        form = EntryForm()
    return render(request, 'addentry.html', {'form': form})