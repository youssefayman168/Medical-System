from rest_framework import serializers
from ..models import Export, Order

class ExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Export
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"