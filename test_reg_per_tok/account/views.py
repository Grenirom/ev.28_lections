from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from rest_framework import generics, permissions





































# from account.serializers import RegistrationSerializer, UserListSerializer, UserDetailSerializer

# class UserRegistrationView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegistrationSerializer
#
#
# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer
#     permissions = (permissions.IsAuthenticated(), )
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer
#     permissions = (permissions.IsAuthenticated(), )
#
#
# class UserLogOutView(LogoutView):
#     permission_classes = (permissions.IsAuthenticated, )
