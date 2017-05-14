# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from api.serializers import FeatureSerializer
from api.models import Feature

from django.shortcuts import render


class FeatureView(generics.ListCreateAPIView):
    """
    View to create and list features
    Accepts GET and POST requests
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new feature."""
        serializer.save()


class FeatureDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
