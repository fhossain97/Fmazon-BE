from django.db import models

# Create your models here.

class Item(models.Model):
    name: models.CharField(max_length=100)
    quantity: models.IntegerField()
    price: models.IntegerField()
    description: models.CharField()

    def _str_(self):
        return self.name

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    title: models.CharField(max_length=100)
    comment: models.CharField(max_length=300)

    def _str_(self):
        return self.title