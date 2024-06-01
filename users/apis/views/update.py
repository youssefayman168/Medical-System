from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from ...models import User
from users.apis.serializers import UserSerializer
from globals.permissions import OnlyAdmins

@api_view(["PUT"])
@permission_classes([OnlyAdmins])
def update_user(request, user_id): 
    try :
        
        try :
            user = User.objects.get(id=user_id)
        except User.DoesNotExist :
            return Response({'message':"user does not found"},status=status.HTTP_404_NOT_FOUND)
        
        try:
            serializer = UserSerializer(user,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message':'تم تحديث البيانات بنجاح'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": f"حدث خطأ اثناء تحديث بيانات المستخدم" 
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        print(error)
        return Response({
            'message' : f'an error occurred : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
    