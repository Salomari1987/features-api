# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from api.models import Feature
from datetime import datetime

class FeatureModelTestCase(TestCase):
    """
    This class defines test cases for the Feature model
    """

    def setUp(self):
        self.feature_title = "Write the Features APP"
        self.feature_description = "Feature request description"
        self.feature_target_date = datetime(year=2018, month=6, day=1)
        self.feature_ticket_url = "www.example.com"
        self.feature_product_area = "Policies"
        self.feature = Feature(title=self.feature_title,
                            description=self.feature_description,
                            target_date=self.feature_target_date,
                            ticket_url=self.feature_ticket_url,
                            product_area=self.feature_product_area)

    def test_model_creates_a_feature(self):
        before_count = Feature.objects.count()
        self.feature.save()
        after_count = Feature.objects.count()
        self.assertNotEqual(before_count, after_count)
