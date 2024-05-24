from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from ...models import User

@api_view(['POST',])
@permission_classes([permissions.IsAdminUser])
def create_user(request):
    data = request.data
    if not data:
        return Response({
            "message": "من فضلك ادخل بيانات المستخدم لانشاؤه"
        }, status=status.HTTP_100_CONTINUE)
    
    username = data.get("username")
    email = data.get("email")
    job_title = data.get("job_title")
    national_id = data.get("national_id")
    password = data.get("password")
    is_admin = data.get("is_admin")

    if not username:
        return Response({
            "message": "من فضلك ادخل اسم المستخدم"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not email:
        return Response({
            "message": "من فضلك ادخل بريد المستخدم"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not job_title:
        return Response({
            "message": "من فضلك ادخل وظيفة المستخدم"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not national_id:
        return Response({
            "message": "من فضلك ادخل رقم هوية المستخدم"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not password:
        return Response({
            "message": "من فضلك ادخل كلمة سر المستخدم"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    username_exists = User.objects.filter(username=username).exists()
    email_exists = User.objects.filter(email=email).exists()

    if username_exists:
        return Response({
            "message": "يوجد مستخدم بالفعل بهذا الاسم"
        }, status=status.HTTP_400_BAD_REQUEST)

    if email_exists:
        return Response({
            "message": "يوجد مستخدم بالفعل بهذا البريد"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        User.objects.create(
            username=username,
            email=email,
            job_title=job_title,
            national_id=national_id,
            password=make_password(password),
            is_admin=is_admin
        )
        return Response({
            "message": "تم انشاء المستخدم بنجاح!"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "حدث خطأ اثناء انشاء المستخدم...حاول مرة اخري لاحقاً"
        }, status=status.HTTP_400_BAD_REQUEST)