from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Item, Review, Photo
from rest_framework import generics
from .serializers import ItemSerializer, ReviewSerializer
import uuid
import boto3
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'fmazon'

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

def add_photo(request, item_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, item_id=item_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', item_id=item_id)
