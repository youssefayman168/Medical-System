from rest_framework import serializers
from ..models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "job_title", "national_id", "is_admin", "pk")

class LoginSerializer (serializers.Serializer) : 
    email = serializers.EmailField()
    password = serializers.CharField()
    tokens = {}

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try : 
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'message':"invalid email"})
        
        if not user.check_password(password) : 
            raise serializers.ValidationError({'message':"invalid password"})
        
        token = RefreshToken.for_user(user)
        self.tokens = {
            'refresh' : str(token),
            'access' : str(token.access_token),
        }
        return attrs