from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import PaitentSerializer
from ...models import Paitent

@api_view(["GET",])
@permission_classes([permissions.IsAdminUser])
def search_patients(request, doc_num):
    try:
        paitents = Paitent.objects.filter(document_number__startswith=doc_num).order_by('-added_at')
        serializer = PaitentSerializer(paitents, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حصل خطأ اثناء البحث في بيانات المرضي"
        }, status=status.HTTP_400_BAD_REQUEST)