from rest_framework.decorators import permission_classes, api_view
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from patients.models import Paitent
from receipets.models import Receipet
from patients.apis.serializers import PaitentSerializer
from receipets.apis.serializers import ReceipetSerializer

@api_view(["GET",])
@permission_classes([permissions.IsAdminUser])
def get_patient_report(request, document_number):
    try:
        patient = Paitent.objects.get(document_number=document_number)
    except Paitent.DoesNotExist:
        return Response({
            "message": "المريض ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        receipts = Receipet.objects.filter(patient=patient)
    except Exception as e:
        return Response({
            "message": "حدث خطأ اثناء جلب الاستلامات"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        patient_data = PaitentSerializer(patient, many=False).data
        receipts_data = ReceipetSerializer(receipts, many=True).data
        return Response({
            "data": {
                "patient": patient_data,
                "receipts": receipts_data,
            }
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حدث خطأ اثناء جلب التقرير"
        }, status=status.HTTP_400_BAD_REQUEST)
