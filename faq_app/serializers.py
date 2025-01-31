from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__' # Include all fields in the API response

# This serializer is used to convert the FAQ data to a JSON response