from rest_framework import serializers
from api.models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    """
    Features Serializer class to return the model instance in json format for api requests.
    """
    class Meta:
        model = Feature
        fields = ('id', 'title', 'description', 'target_date', 'ticket_url', 'product_area', 'priority', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')
