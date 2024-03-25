# myapp/management/commands/export_menu_data.py
import json
from decimal import Decimal
from django.core.management.base import BaseCommand
from content.models import MenuCategory, MenuItem

class Command(BaseCommand):
    help = 'Export menu data to JSON files'

    def handle(self, *args, **options):
        menu_data = {}
        categories = MenuCategory.objects.all()
        for category in categories:
            items = MenuItem.objects.filter(category=category).values('name', 'description', 'price')
            # Convert Decimal objects to floats
            items = [{**item, 'price': float(item['price'])} for item in items]
            menu_data[category.name] = items

        with open('menu_data.json', 'w') as f:
            json.dump(menu_data, f, indent=2)

        self.stdout.write(self.style.SUCCESS('Menu data exported successfully to menu_data.json'))
