from django.db import models

# Create your models here.

class Product(models.Model):
    NEW = 'N'
    USED = 'U'
    STATE_CHOICES = (
        (NEW, 'New'),
        (USED, 'Used'),
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default=NEW)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name