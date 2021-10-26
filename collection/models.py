from django.db import models

# Create your models here.
class Entry(models.Model):
    item = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    author = models.CharField(max_length=255)

    @property
    def __str__(self):
        return "%s: %d %s" % (self.author, self.count, self.item)

class RareDropTableItems(models.Model):
    item = models.CharField(max_length=100)
    itemAlias = models.CharField(max_length=100, primary_key=True)

    @property
    def __str__(self):
        return "%s" % (self.item)