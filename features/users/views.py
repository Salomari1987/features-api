# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from users.serializers import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        data = {
            "username": serializer.data["username"],
            "token": token.key
        }

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                data={
                    "username": user.username,
                    "token": TokenSerializer(token).data["auth_token"]
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserLogoutAPIView(APIView):

    def post(self, request, *args, **kwargs):
        Token.objects.filter(user=request.user).delete()

        return Response(status=status.HTTP_200_OK)
