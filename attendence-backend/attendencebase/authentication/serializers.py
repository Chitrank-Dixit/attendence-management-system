from rest_framework import serializers
from authentication.models import User

__author__ = 'chitrankdixit'


class UserSerializer(serializers.ModelSerializer):
    """
        This is the User serializer to get user data
    """
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'password', 'first_name', 'last_name', 'email', 'mobile_number',
                  'avatar_url', 'gender', 'age',)


class UserCreateSerializer(serializers.ModelSerializer):
    """
        This is the User serializer to get user data
    """
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'password', 'first_name', 'last_name', 'email', 'mobile_number',
                  'avatar_url', 'gender', 'age',)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user
