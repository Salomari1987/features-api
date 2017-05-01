# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Feature(models.Model):
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
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
