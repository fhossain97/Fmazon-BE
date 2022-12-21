from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

class Item:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, quantity, description):
    self.name = name
    self.quantity = quantity
    self.description = description


items = [
  Item('Lolo', 2, 'foul little demon'),
  Item('Sachi', 3, 'diluted tortoise shell'),
  Item('Raven', 4, '3 legged cat')
]

def home(request):
    return HttpResponse('<h1>Hello Friends!< /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def items_index(request):
    return render(request, 'items/items.html', {'items': items})