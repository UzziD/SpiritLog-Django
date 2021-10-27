from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Entry
from .models import RareDropTableItems
from .forms import EntryForm
# Create your views here.

def index(request):
    allEntries = Entry.objects.all()
    output = ', '.join([e.__str__ for e in allEntries])
    return HttpResponse(output)

def addEntry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            item = RareDropTableItems.objects.filter(itemAlias=form.item).first()  #grab item name based on user's input item
            itemEntry = form.save(commit=False)                     #save the non validated form to change to proper item name
            itemEntry.item = item
            itemEntry.save()
            return HttpResponseRedirect('/collection/')

    else:
        form = EntryForm()
    return render(request, 'addentry.html', {'form': form})