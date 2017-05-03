from rest_framework import serializers
from api.models import Feature

class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = ('id', 'title', 'description', 'target_date', 'ticket_url', 'product_area', 'priority', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')
