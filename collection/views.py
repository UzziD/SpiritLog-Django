from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Entry
from .models import RareDropTableItems
from .forms import EntryForm
# Create your views here.

def index(request):
    allEntries = Entry.objects.all()
    output = ', '.join([e.__str__() for e in allEntries])
    return HttpResponse(output)

def addEntry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            try:
                formItem = form['item'].value()
                RDTItem = RareDropTableItems.objects.get(itemAlias=formItem)  #grab item name based on user's input item
                item = getattr(RDTItem, 'item')
                itemEntry = form.save(commit=False)                     #save the non validated form to change to proper item name
                itemEntry.item = item
                itemEntry.save()
                return HttpResponseRedirect('/collection/')
            except Exception as e:
                return HttpResponse(str(form['item'].value()) + " returned error: {}".format(e))
    else:
        form = EntryForm()
    return render(request, 'addentry.html', {'form': form})