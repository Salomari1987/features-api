# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from api.serializers import FeatureSerializer
from api.models import Feature

from django.shortcuts import render

class FeatureView(generics.ListCreateAPIView):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new feature."""
        serializer.save()
