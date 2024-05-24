from rest_framework import status, decorators
from rest_framework.response import Response
from ....models import User, OTPCode

@decorators.api_view(["POST",])
def reset_password(request):
    data = request.data

    if not data:
        return Response({
            "message": "Data can't be empty"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    otp_code = data.get("otp_code")
    email = data.get("email")
    new_password = data.get("new_password")

    if not email:
        return Response({
            "message": "Please enter email"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not otp_code:
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
        otp = OTPCode.objects.filter(user=user, otp=otp_code).last()
        if not otp:
            return Response({
            "message": "There's no OTP for you to reset your password, did you go through this page by mistake? or you can ask for OTP first"
        }, status=status.HTTP_404_NOT_FOUND)
    
        if not otp.verified:
            return Response({
                "message": "Your OTP isn't verified, please go to the previous page and verify it first"
            }, status=status.HTTP_400_BAD_REQUEST)

        if not new_password:
            return Response({
                "message": "Please enter a new password"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if user.check_password(new_password):
            return Response({
                "message": "Please enter a new password"
            }, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        otp.delete()
        return Response({
            "message": "Password was set successfully"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while resetting your password, please try again."
        }, status=status.HTTP_400_BAD_REQUEST)
    
        