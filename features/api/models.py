# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import F


class Feature(models.Model):
    """
    Feature model
    example:
    {
        "title": "Add OAuth authentication/authorization",
        "description": "3 Legged OAuth through Twitter and Facebook",
        "target_date": "5-8-2017",
        "ticket_url": "http://features.herokuapp.com/features/1467"
        "product_area": "R",
        "priority": "2"
    }
    """
    PRODUCT_AREA_CHOICES = (
        ('P', 'Policies'),
        ('B', 'Billing'),
        ('C', 'Claims'),
        ('R', 'Reports'),
    )

    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    target_date = models.DateField(blank=True)
    ticket_url = models.URLField()
    product_area = models.CharField(
        max_length=2,
        choices=PRODUCT_AREA_CHOICES,
    )
    priority = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        """
        Method overrides model save method to increment priority of an object that equals object to be saved.
        If an object's priority is increased and then it matches the changed object,
        then the save method of the changed object is also called
         i.e. the process is recursive
        """
        try:
            feature = Feature.objects.get(priority=self.priority)
            feature.priority = feature.priority + 1
            feature.save()
        except Feature.DoesNotExist:
            pass

        super(Feature, self).save(*args, **kwargs)
