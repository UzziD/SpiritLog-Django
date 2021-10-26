from django.contrib import admin

# Register your models here.
from .models import Entry
from .models import RareDropTableItems
admin.site.register(Entry)
admin.site.register(RareDropTableItems)