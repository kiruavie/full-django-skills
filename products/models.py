from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    price = models.FloatField()
    active = models.BooleanField()
    live = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    

    

    