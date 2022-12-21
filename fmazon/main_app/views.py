from django.http import HttpResponse
from .models import Item, Review
from rest_framework import generics
from .serializers import ItemSerializer, ReviewSerializer

# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello Friends!< /ᐠ｡‸｡ᐟ\ﾉ</h1>')

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
