from django.db import models

# Create your models here.
class Manufacturer (models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class ShoeType (models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style

class ShoeColor (models.Model):
    RED = 'R'
    ORANGE = 'O'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VIOLET = 'V'
    WHITE = 'W'
    BLACK = 'BK'
    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ]
    color_name = models.CharField(
        max_length=6,
        choices=COLOR_CHOICES,
        default=WHITE,
        )

    def __str__(self):
        return self.color_name

class Shoe (models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length = 100)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name = 'manufacturer')
    color = models.ForeignKey(
        ShoeColor,
        on_delete=models.CASCADE,
        related_name = 'shoe_color')
    material = models.CharField(max_length = 100)
    shoe_type = models.ForeignKey(
        ShoeType,
        on_delete=models.CASCADE,
        related_name = 'shoe_type')
    fasten_type = models.CharField(max_length = 100)

#Joe was raised in the Savanna by the indigenous tribe, Zulu.
#Due to Joe's scruffy appearance he was nicknamed 'The White Jackal'.
#He would later don this moniker due to the devastations caused by poachers in the Savanna.
#By day just a seemless Computer Programmer, by night a hunter who hunts the hunters.