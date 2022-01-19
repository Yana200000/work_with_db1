import csv

from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('D:\phones.csv') as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                phone = Phone(
                    id=int(row['id']),
                    name=row['name'],
                    image=row['image'],
                    price=int(row['price']),
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'],
                    slug=slugify(row['name'])
                )
                phone.save()


