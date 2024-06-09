from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import PaitentSerializer
from ...models import Paitent
from globals.track_activity import track_activity
from activity.models import Activity

@api_view(['GET',])
@permission_classes([permissions.IsAdminUser])
def delete_patient(request, patient_id):
    user = request.user
    try:
        patient = Paitent.objects.get(pk=patient_id)
    except Paitent.DoesNotExist:
        return Response({
            "message": "المريض ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        patient.delete()
        try:
                Activity.objects.create(
                        content=f"تم حذف مريض بواسطة {user.username}",
                        made_by=user
                    )
        except Exception as e:
                return Response({
                    "message": "حدث خطأ اثناء حذف المريض"
                })      

        return Response({
            "message": "تم حذف المريض بنجاح"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "حصل خطأ اثناء حذف المريض"
        }, status=status.HTTP_400_BAD_REQUEST)
