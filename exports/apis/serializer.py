from rest_framework import serializers
from ..models import Export, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("prod_name", "quantity")

class ExportSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)
    class Meta:
        model = Export
        fields = "__all__"

