from rest_framework import serializers
from receipets.models import Receipet
from patients.apis.serializers import PaitentSerializer
class ReceipetSerializer(serializers.ModelSerializer):
    patient = PaitentSerializer(read_only=True, many=False)
    class Meta:
        model = Receipet
        fields = "__all__"
        