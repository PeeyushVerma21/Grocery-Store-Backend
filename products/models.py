from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    image_url = models.URLField(blank=True, null=True)
    sold_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
