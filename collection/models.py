from django.db import models

# Create your models here.
class entry(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    item = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    author = models.CharField(max_length=255)

    @property
    def __str__(self):
        return "%s: %d %s" % (self.author, self.count, self.item)