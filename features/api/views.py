# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from api.serializers import FeatureSerializer
from api.models import Feature
from api.permissions import IsOwnerOrStaff

from rest_framework import permissions


class FeatureView(generics.ListCreateAPIView):
    """
    View to create and list features
    Accepts GET and POST requests
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrStaff,
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new feature."""
        serializer.save(owner=self.request.user)


class FeatureDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrStaff)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

