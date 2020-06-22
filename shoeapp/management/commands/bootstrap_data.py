from django.core.management.base import BaseCommand, CommandError
from shoeapp.models import ShoeColor, ShoeType

class Command(BaseCommand):
    def handle(self, *args, **options):
        shoe_choices = ['sneaker', 'boot', 'sandal', 'dress', 'other', ]
        shoe_color = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Black', ]
        for color in shoe_color:
            ShoeColor.objects.create(color_name=color)
        for shoe_types in shoe_choices:
            ShoeType.objects.create(style=shoe_types)
        