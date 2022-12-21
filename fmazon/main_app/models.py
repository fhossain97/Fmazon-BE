from django.db import models
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    name: models.CharField(max_length=100, null=True)
    quantity: models.IntegerField()
    price: models.IntegerField()
    description: models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'item_id': self.id})

    def _str_(self):
        return f'{self.name}'

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    title: models.CharField(max_length=100)
    comment: models.CharField(max_length=300)

    def _str_(self):
        return f'{self.title}'