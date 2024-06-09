from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import PaitentSerializer
from globals.track_activity import track_activity
from activity.models import Activity

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_patient(request): 
    user = request.user
    
    try:
        serializer = PaitentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            try:
                Activity.objects.create(
                        content="تم انشاء مريض جديد حديثاً",
                        made_by=user
                    )
            except Exception as e:
                    return Response({
                        "message": "حدث خطأ اثناء انشاء المريض"
                    })            
            return Response({
                "message": "تم اضافة المريض"
            },status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({
            "message": "حدث خطأ اثناء اضافة المريض...الرجاء المحاولة مرة اخري"
        },status=status.HTTP_400_BAD_REQUEST)

    except Exception as error :
        return Response({
            "message" : f'an error accoured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
    