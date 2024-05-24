from rest_framework import serializers
from receipets.models import Receipet

class ReceipetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipet
        fields = "__all__"
        