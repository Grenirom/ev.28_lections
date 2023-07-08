from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm', 'first_name', 'last_name', 'username', 'avatar')

    def validate(self, attrs):
        password = attrs['password']
        password_confirm = attrs.pop('password_confirm')
        if password_confirm != password:
            raise ValueError('Passwords did not match! Please check the passwords again')
        validate_password(password)
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user