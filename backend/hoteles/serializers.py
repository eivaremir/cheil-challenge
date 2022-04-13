from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            "hotel_id",
            "category",
            "name",
            "slug",
            "description",
            "score",
            "price_per_night",
            "thumbnail",
            "date_added"
            
        )