from django.core.management import BaseCommand
from catalog.models import Product, Version


class Command(BaseCommand):

    def handle(self, *args, **options):

        products = [
            {'name': 'мясо', 'description': 'свежее мясо', 'price': 22},
            {'name': 'чай', 'description': 'ароматный чай', 'price': 33},
            {'name': 'кофе', 'description': 'вкусный кофе', 'price': 44}
        ]
        products_list = []
        for item in products:
            products_list.append(Product(**item))

        Product.objects.bulk_create(products_list)

        versions = [
            {'number': 1, 'name': '11', 'product_id': Product.objects.get(pk=1)},
            {'number': 2, 'name': '22', 'product_id': Product.objects.get(pk=2)},
            {'number': 3, 'name': '33', 'product_id': Product.objects.get(pk=3)}
        ]
        versions_list = []
        for item in versions:
            versions_list.append(Version(**item))

        Version.objects.bulk_create(versions_list)
