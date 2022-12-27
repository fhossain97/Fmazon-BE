from django.db import models
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default='No Description Found')
    url= models.TextField(default='No Image')

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'item_id': self.id})

    def _str_(self):
        return f'{self.name}'

class Review(models.Model):
    title = models.CharField(max_length=100, null=True)
    comment = models.CharField(max_length=300, default='No Comment Yet!')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')

    def _str_(self):
        return f'{self.title}'

class Photo(models.Model):
    url = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def _str_(self):
        return f"Photo for item_id: {self.item_id} @{self.url}"