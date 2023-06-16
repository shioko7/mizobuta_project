import os
import json
from django.core.management.base import BaseCommand
from mizobuta.models import Prefecture

class Command(BaseCommand):
    help = 'Load prefecture data from JSON file'

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prefecture_data.json')
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            for prefecture in data:
                Prefecture.objects.create(code=prefecture['code'], name=prefecture['name'])
        self.stdout.write(self.style.SUCCESS('Prefecture data loaded successfully.'))
