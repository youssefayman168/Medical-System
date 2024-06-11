from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from exports.models import Export, Order
from exports.apis.serializer import ExportSerializer, OrderSerializer
from activity.models import Activity

@api_view(['DELETE',])
@permission_classes([permissions.IsAdminUser])
def delete_export(request, export_id):
    user = request.user

    try:
        export = Export.objects.get(pk=export_id)
    except Export.DoesNotExist:
        return Response({
            "message": "التوريد ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        export.delete()
        try:
            Activity.objects.create(
                content=f"تم حذف توريد بواسطة {user.username}",
                made_by=user
            )
        except Exception as e:
            return Response({
                "message": "حدث خطأ اثناء الحذف...رجاء حاول مرة اخري"
            })
        return Response({
            "message": "تم حذف التوريد بنجاح "
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حصل خطأ اثناء جذف التوريد"
        }, status=status.HTTP_400_BAD_REQUEST)