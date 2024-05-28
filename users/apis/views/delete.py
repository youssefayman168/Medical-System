from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from ...models import User


@api_view(['DELETE',])
@permission_classes([permissions.IsAdminUser])
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({
            "message": "المستخدم ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        user.delete()
        return Response({
            "message": "تم حذف المستخدم",
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "حدث خطأ اثناء حذف المستخدم برجاء المحاولة مرة اخري"
        }, status=status.HTTP_400_BAD_REQUEST)