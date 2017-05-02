# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from api.models import Feature
from datetime import datetime
from rest_framework import status
from django.core.urlresolvers import reverse

class FeatureModelTestCase(TestCase):
    """
    This class defines test cases for the Feature model
    """

    def setUp(self):
        self.feature_title = "Write the Features APP"
        self.feature_description = "Feature request description"
        self.feature_target_date = "2018-08-12"
        self.feature_ticket_url = "http://www.example.com"
        self.feature_product_area = "P"
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


class FeatureViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.feature_data = {
            'title': 'Feature view title test',
            'description': 'Description of the Feature request',
            'target_date': "2018-08-21",
            'ticket_url': 'http://www.example.com',
            'product_area': 'P'
        }
        self.response_post = self.client.post(
            reverse('features'),
            self.feature_data,
            format='json'
        )
        self.response_get = self.client.get(
            reverse('features'),
            format='json'
        )

    def test_api_create_feature(self):
        self.assertEqual(self.response_post.status_code, status.HTTP_201_CREATED)

    def test_api_create_feature_content(self):
        self.assertEqual(self.response_post.data["description"], self.feature_data['description'])
        self.assertEqual(self.response_post.data["product_area"], self.feature_data['product_area'])

    def test_api_get_features(self):
        self.assertEqual(self.response_get.status_code, status.HTTP_200_OK)

    def test_api_get_features_body(self):
        self.client.post(
            reverse('features'),
            self.feature_data,
            format='json'
        )
        response_get_all = self.client.get(
            reverse('features'),
            format='json'
        )
        self.assertEqual(len(response_get_all.data), 2)
        self.assertEqual(response_get_all.data[1]['id'], 2)
