from rest_framework import serializers
from .models  import*

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = vehicleSearchRequest, vehicleSearchResponse
        fields = "__all__"