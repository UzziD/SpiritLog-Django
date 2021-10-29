from django.shortcuts import render

def index(request):
    return render(None, 'homepage/index.html')
