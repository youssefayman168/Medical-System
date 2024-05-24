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
            "message": "Data can't be empty"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    email = data.get("email")

    if not email:
        return Response({
            "message": "Please enter email"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    is_user_exists = User.objects.filter(email=email).exists()

    if not is_user_exists:
        return Response({
            "message": "This email doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)
    
    
    try:
        send_otp.delay(email)
        return Response({
            "message": "An OTP was sent to your email, please check it out!"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while sending the email, please try again."
        }, status=status.HTTP_400_BAD_REQUEST)
