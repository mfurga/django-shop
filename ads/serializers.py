from rest_framework import serializers

from .models import Ad


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'slug', 'category', 'description', 'condition',
                  'location', 'price', 'phone_number', 'pub_date', 'author')
