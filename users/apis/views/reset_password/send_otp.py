from rest_framework import status, decorators
from rest_framework.response import Response
from ....models import User
from ....tasks import send_otp

"""
1. Send OTP
2. Verify the OTP
3. Reset Password:
    - First Check The OTP in the Params
    - If It Was Verified Then Reset Then Delete the OTP
    - If It Wasn't, Don't Go On
"""


@decorators.api_view(["POST",])
def send_reset_otp(request):
    data = request.data

    if not data:
        return Response({
            "message": "لا يمكن للبيانات ان تكون فارغة"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    email = data.get("email")

    if not email:
        return Response({
            "message": "ادخل البريد من فضلك"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    is_user_exists = User.objects.filter(email=email).exists()

    if not is_user_exists:
        return Response({
            "message": "هذا البريد ليس مٌسجل "
        }, status=status.HTTP_404_NOT_FOUND)
    
    
    try:
        send_otp.delay(email)
        return Response({
            "message": "تم ارسال رمز للبريد الالكتروني الخاص بك!"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": f"an error occurred while sending the email, please try again. {e}"
        }, status=status.HTTP_400_BAD_REQUEST)
