from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        self.process()

    @transaction.atomic
    def process(self):
        print("Hello World")
