from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm
# Create your views here.

def index(request):
    allEntries = Entry.objects.all()
    output = ', '.join([e.__str__ for e in allEntries])
    return HttpResponse(output)

def addEntry(request):
    if request.method == 'Post':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collection/')
    else:
        form = EntryForm()
    return render(request, 'addentry.html', {'form', form})