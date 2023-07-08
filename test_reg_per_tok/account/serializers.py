from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

















# class RegistrationSerializer(serializers.ModelSerializer):
#     first_name = serializers.CharField(max_length=50, required=True)
#     last_name = serializers.CharField(max_length=50, required=True)
#     email = serializers.EmailField()
#     password = serializers.CharField(min_length=8, write_only=True, required=True)
#     confirm_password = serializers.CharField(min_length=8, write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'username', 'password', 'confirm_password')
#
#     def validate(self, validated_data):
#         print(validated_data, '1111111111111111111111111')
#         password2 = validated_data.pop('confirm_password')
#         if password2 != validated_data['password']:
#             raise serializers.ValidationError('Passwords didn\'t match!')
#         validate_password(validated_data['password'])
#         return validated_data
#
#     def validate_first_name(self, value):
#         # print(value, '*****************************')
#         if not value.istitle():
#             raise serializers.ValidationError('First name must start with title letter!')
#         return value
#
#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#
#
# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username')
#
#
# class UserDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name', 'email')
