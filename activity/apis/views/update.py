from globals.permissions import OnlyAdmins
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from activity.models import Activity

@api_view(["PUT"])
@permission_classes([OnlyAdmins])
def read_all(request):
    try:
        activities = Activity.objects.all().order_by("-sent_at")
    except Exception as e:
        print(e)
        return Response({
            "message": "حدث خطأ اثناء جلب الاشعارات"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        is_updated = False
        for activity in activities:
            activity.read = True
            activity.save()
            is_updated = True

        if is_updated:
            return Response({
                "message": "تم قراءة جميع الاشعارات"
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "لم يتم قراءة اي رسالة او ربما لا يوجد رسائل لقرائتها"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "لم يتم قراءة الرسايل لحدوث خطأ معين...حاول مرة اخري"
        }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PUT"])
@permission_classes([OnlyAdmins])
def read_activity(request, activity_id):
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        return Response({
            "message": "لم يتم العثور علي الاشعار!"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        activity.read = True
        activity.save()
        return Response({
            "message": "تم قراءة الرسالة بنجاح !"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "لم يتم قراءة الرسالة لحدوث خطأ معين...حاول مرة اخري"
        }, status=status.HTTP_400_BAD_REQUEST)