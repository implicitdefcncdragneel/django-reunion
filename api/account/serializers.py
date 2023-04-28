from api.account.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AuthenticateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email","password"]
        extra_kwargs = {'password' : {'write_only': True},}

    def create(self, validated_data):
        member = User.objects.create_user(email=validated_data['email'])
        member.set_password(validated_data['password'])
        member.save()
        return member
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email"]