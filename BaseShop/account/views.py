from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from . import serializers
from .send_act_code import send_activation_email
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

User = get_user_model()


class AccountViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
    permission_classes = (permissions.AllowAny, )

    @action(['POST'], detail=False)
    def registration(self, request, *args, **kwargs):
        serializer = serializers.RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_activation_email(user.email, user.activation_code)
            except Exception as i:
                print(i, '===========')
                return Response({'msg': 'Registered, but issues with email address!',
                                 'data': serializer.data}, status=200)
            return Response(serializer.data, status=201)

    @action(['GET'], detail=False, url_path='activate/(?P<uuid>[0-9A-Fa-f-]+)')
    def activate(self, request, uuid):
        try:
            user = User.objects.get(activation_code=uuid)
        except User.DoesNotExist:
            return Response({'msg': 'Invalid link, or link has already expired!'}, status=400)
        user.is_active = 'True'
        user.activation_code = ''
        user.save()
        return Response({'msg': 'Successfully activated your account!'}, status=200)


class Login(TokenObtainPairView):
    permission_classes = (permissions.AllowAny, )


class Refresh(TokenRefreshView):
    permission_classes = (permissions.AllowAny, )

