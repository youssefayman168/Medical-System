from rest_framework import status, decorators
from rest_framework.response import Response
from users.apis.serializers import LoginSerializer

@decorators.api_view(['POST'])
def login(request) : 
    try :
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid() : 
            return Response(serializer.tokens,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as error :
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)