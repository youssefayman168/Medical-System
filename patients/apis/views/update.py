from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from ..serializers import PaitentSerializer
from globals.track_activity import track_activity
from ...models import Paitent
from activity.models import Activity

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def update_patient(request, patient_id):
    user= request.user 
    try:
        try: 
            patient = Paitent.objects.get(id=patient_id)
        except Paitent.DoesNotExist:
            return Response({
                'message' : "المريض ليس موجود"
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer = PaitentSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                Activity.objects.create(
                        content=f"تم نحديث بيانات مريض بواسطة {user.username}",
                        made_by=user
                    )
            except Exception as e:
                    return Response({
                        "message": "حدث خطأ اثناء حذف المريض"
                    })   

            return Response({
                "message": "تم تحديث المريض"
            },status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response({
            "message": "حدث خطأ اثناء تحديث المريض...الرجاء المحاولة مرة اخري"
        },status=status.HTTP_400_BAD_REQUEST)

    except Exception as error:
        return Response({
            "message" : "حدث خطأ اثناء تحديث بيانات المريض"
        },status=status.HTTP_400_BAD_REQUEST)
    
