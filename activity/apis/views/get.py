from globals.permissions import OnlyAdmins
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from activity.models import Activity
from ..serializers import ActivitySerializer

@api_view(["GET",])
@permission_classes([OnlyAdmins])
def get_activities(request):
    try:
        activities = Activity.objects.all().order_by("-sent_at")
        serializer = ActivitySerializer(activities, many=True).data
        return Response({
            "data": serializer
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "حدث خطأ اثناء جلب الاشعارات"
        }, status=status.HTTP_100_CONTINUE)