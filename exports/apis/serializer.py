from rest_framework import serializers
from ..models import Export, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class ExportSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Export
        fields = "__all__"

    def get_orders(self, obj):
        orders = Order.objects.filter(export=obj)
        serializer = OrderSerializer(orders, many=True).data
        return serializer
