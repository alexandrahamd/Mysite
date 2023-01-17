from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category = [
            {'name': 'мясо', 'description': 'свежее мясо'},
            {'name': 'чай', 'description': 'ароматный чай'},
            {'name': 'кофе', 'description': 'вкусный кофе'}
        ]
        category_list = []
        for item in category:
            category_list.append(Category(**item))

        Category.objects.bulk_create(category_list)
