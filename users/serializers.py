from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'avatar', 'password')