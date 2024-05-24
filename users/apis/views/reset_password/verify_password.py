"""
1. Get the user by the email
2. check if the OTP exists for this user
3. Check if the OTP is valid
4. Check if the content matches the OTP content
2. If it's valid then
"""
from rest_framework import status, decorators
from rest_framework.response import Response
from ....models import User, OTPCode
from django.utils import timezone
now = timezone.now()

@decorators.api_view(["POST"])
def verify_otp(request):
    data = request.data

    if not data:
        return Response({
            "message": "Data can't be empty"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    otp = data.get("otp")
    email = data.get("email")

    if not email:
        return Response({
            "message": "Please enter email"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not otp:
        return Response({
            "message": "Please enter the OTP"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({
            "message": "Couldn't find the user"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        otp_code = OTPCode.objects.filter(user=user, otp=otp).last()
        if not otp_code:
            return Response({
            "message": "We haven't sent any OTP until the moment or maybe you typed the OTP wrong!"
        }, status=status.HTTP_404_NOT_FOUND)
        if now > otp_code.valid_for:
            return Response({
                "message": "The OTP you entered isn't valid, please head back and generate a new one."
            }, status=status.HTTP_400_BAD_REQUEST)
        otp_code.verified = True
        otp_code.save()
        return Response({
            "message": "OTP verified successfully, now you can reset your password safely"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while sending the email, please try again."
        }, status=status.HTTP_400_BAD_REQUEST)
        
