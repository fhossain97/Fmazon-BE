from rest_framework import serializers
from .models import Item, Review
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User=get_user_model()

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
        fields= ('id', 'name', 'quantity', 'price', 'description', 'item_url', 'review', 'url')

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


class UserSerializer(serializers.ModelSerializer):

    assword = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)