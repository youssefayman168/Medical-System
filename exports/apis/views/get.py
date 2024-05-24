from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from exports.models import Export, Order
from exports.apis.serializer import ExportSerializer, OrderSerializer


@api_view(['GET',])
@permission_classes([permissions.IsAdminUser])
def get_all(request):
    try:
        exports = Export.objects.all()
        serializer = ExportSerializer(exports, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حصل خطأ اثناء جلب التوريدات"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@permission_classes([permissions.IsAdminUser])
def get_export(request, export_id):
    try:
        export = Export.objects.get(pk=export_id)
    except Export.DoesNotExist:
        return Response({
            "message": "التوريد ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        serializer = ExportSerializer(export, many=False)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حصل خطأ اثناء جلب بيانات التوريد"
        }, status=status.HTTP_400_BAD_REQUEST)