from rest_framework import serializers
from ..models import Activity
from users.apis.serializers import UserSerializer

class ActivitySerializer(serializers.ModelSerializer):
    made_by = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Activity
        fields = "__all__"