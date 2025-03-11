from django.core.management.base import BaseCommand
from django.db import transaction


import yaml

BASE_PATH = "app/management/seed"


class Command(BaseCommand):
    help = "Load seed data. It can include extra info without duplicate others"

    def handle(self, *args, **options):
        self.data_seed()

    @transaction.atomic
    def data_seed(self):
        with open(f"{BASE_PATH}/seed.yml") as file:
            try:
                content = yaml.safe_load(file)

                for _ in content:
                    # Add seed logic
                    self.stdout.write("Add seed")

                self.stdout.write("All seeds added")

            except yaml.YAMLError as exc:
                print(exc)
