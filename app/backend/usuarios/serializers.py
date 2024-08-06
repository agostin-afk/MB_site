from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MyUserBase
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')
        def validate(self, data):
            username = data.get('username')
            password = data.get('password')
            # email = data.get('email')
            if username and password:
                user = User.objects.filter(username=username, password=password)
                print(user)
                if user:
                    print('\n\n\nPassou, Usuario existe\n\n')
                else:
                    print('\n\nNão encontrado\n\n')
            else:
                raise serializers.ValidationError('Preencha todos os campos.')
        
            data['user'] = user
            return data