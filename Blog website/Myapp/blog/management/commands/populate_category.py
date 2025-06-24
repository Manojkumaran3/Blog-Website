from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = "This commands inserts post data"

    def handle(self, *args: Any, **options: Any):

        #Delete exsisting data
        Category.objects.all().delete()
        categories=["Sports","Technology","Science","Art","Food"]
        for category_name in categories:
            Category.objects.create(name = category_name )

        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))