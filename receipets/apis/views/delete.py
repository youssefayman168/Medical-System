from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from globals.track_activity import track_activity
from patients.models import Paitent
from receipets.models import Receipet
from receipets.apis.serializers import ReceipetSerializer


@api_view(["DELETE",])
@permission_classes([permissions.IsAdminUser])
def delete_receipt(request, receipt_id):
    user = request.user
    try:
        receipt = Receipet.objects.get(pk=receipt_id)
    except Receipet.DoesNotExist:
        return Response({
            "message": "لم نستطع العثور علي الاستلام المطلوب"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:    
        receipt.delete()
        track_activity.delay(f"تم حذف استلام بواسطة {user.username}")
        return Response({
            "message": "تم حذف الاستلام بنجاح"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حدث خطأ اثناء جلب الاستلامات"
        }, status=status.HTTP_400_BAD_REQUEST)