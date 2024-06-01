from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from ...models import User
from users.apis.serializers import UserSerializer
from globals.permissions import OnlyAdmins

@api_view(['GET',])
@permission_classes([OnlyAdmins])
def get_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "حدث خطأ اثناء جلب المستخدمين"
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@permission_classes([OnlyAdmins])
def get_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({
            "message": "المستخدم ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        serializer = UserSerializer(user, many=False)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "حدث خطأ اثناء جلب بيانات المستخدم"
        }, status=status.HTTP_400_BAD_REQUEST)