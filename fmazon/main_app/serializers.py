from rest_framework import serializers
from .models import Item, Review

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    review = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        many=True,
        read_only=True
    )

    item_url = serializers.ModelSerializer.serializer_url_field(
        view_name='item_detail'
    )

    class Meta:
        model = Item
        fields= ('id', 'name', 'quantity', 'price', 'description', 'item_url', 'review')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.HyperlinkedRelatedField(
        view_name='item_detail',
        read_only=True
    )

    item_id =  serializers.PrimaryKeyRelatedField(
        queryset = Item.objects.all(),
        source='item'
    )

    class Meta:
        model = Review
        fields= ('id', 'title', 'comment', 'item_id', 'item')