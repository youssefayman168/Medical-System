from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from globals.track_activity import track_activity
from patients.models import Paitent
from receipets.models import Receipet
from receipets.apis.serializers import ReceipetSerializer

@api_view(["GET",])
@permission_classes([permissions.IsAdminUser])
def get_receipts(request):
    try:
        receipts = Receipet.objects.all()
        serializer = ReceipetSerializer(receipts, many=True).data
        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حدث خطأ اثناء جلب الاستلامات"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET",])
@permission_classes([permissions.IsAdminUser])
def get_receipt(request, receipt_id):
    try:
        receipts = Receipet.objects.get(pk=receipt_id)
    except Receipet.DoesNotExist:
        return Response({
            "message": "لم نستطع العثور علي الاستلام المطلوب"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:    
        serializer = ReceipetSerializer(receipts, many=False).data
        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حدث خطأ اثناء جلب الاستلامات"
        }, status=status.HTTP_400_BAD_REQUEST)