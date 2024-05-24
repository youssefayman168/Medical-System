from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import PaitentSerializer
from ...models import Paitent

@api_view(['GET',])
@permission_classes([permissions.IsAdminUser])
def get_all(request):
    try:
        patients = Paitent.objects.all()
        serializer = PaitentSerializer(patients, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حصل خطأ اثناء جلب بيانات المرضي"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@permission_classes([permissions.IsAdminUser])
def get_patient(request, paitent_id):
    try:
        patients = Paitent.objects.get(pk=paitent_id)
    except Paitent.DoesNotExist:
        return Response({
            "message": "المريض ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        serializer = PaitentSerializer(patients, many=False)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حصل خطأ اثناء جلب بيانات المريض"
        }, status=status.HTTP_400_BAD_REQUEST)