# myapp/management/commands/import_menu_data.py
import json
from django.core.management.base import BaseCommand
from content.models import MenuCategory, MenuItem


class Command(BaseCommand):
    help = 'Import menu data from JSON files'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as f:
            menu_data = json.load(f)

        for category_name, items in menu_data.items():
            category, created = MenuCategory.objects.get_or_create(name=category_name)
            for item in items:
                MenuItem.objects.create(
                    name=item['name'],
                    description=item['description'],
                    price=item['price'],
                    category=category
                )

        self.stdout.write(self.style.SUCCESS('Menu data imported successfully'))
