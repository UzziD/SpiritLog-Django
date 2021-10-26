from django.core.management.base import BaseCommand, CommandError
from collection.models import RareDropTableItems
import csv

class Command(BaseCommand):
    help = "Preloads db with data from csv"

    def add_arguments(self, parser):
        parser.add_argument('path', type='str', help='Indicates the path to the csv file')

    def handle(self, *args, **options):
        path = options['path']
        with open(path) as f:
            reader = csv.reader(f)
            next(reader, None) #use this to skip header
            for row in reader:
                _, created = RareDropTableItems.objects.get_or_create(
                    item=row[0],
                    itemAlias=row[1],
                    )
                # creates a tuple of the new object or
                # current object and a boolean of if it was created        