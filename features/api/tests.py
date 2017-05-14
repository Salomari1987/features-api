# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIClient
from api.models import Feature
from rest_framework import status
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User


class FeatureModelTestCase(TestCase):
    """
    This class defines test cases for the Feature model
    """

    def setUp(self):
        self.feature_title = 'Write the Features APP'
        self.feature_description = 'Feature request description'
        self.feature_target_date = '2018-08-12'
        self.feature_ticket_url = 'http://www.example.com'
        self.feature_product_area = 'P'
        user = User.objects.create(username="TheBestGeekInTheWorld")

        self.feature = Feature(
            title=self.feature_title,
            description=self.feature_description,
            target_date=self.feature_target_date,
            ticket_url=self.feature_ticket_url,
            product_area=self.feature_product_area,
            priority=1,
            owner=user
        )

    def test_model_creates_a_feature(self):
        before_count = Feature.objects.count()
        self.feature.save()
        after_count = Feature.objects.count()
        self.assertNotEqual(before_count, after_count)

    def test_model_increments_priorities_two(self):
        self.feature.save()
        feature2 = Feature(
            title=self.feature_title,
            description=self.feature_description,
            target_date=self.feature_target_date,
            ticket_url=self.feature_ticket_url,
            product_area=self.feature_product_area,
            priority=1
        )
        feature2.save()
        self.assertEqual(Feature.objects.get(pk=self.feature.pk).priority, 2)

    def test_model_increments_priorities_for_group(self):
        self.feature.save()
        feature2 = Feature(
            title=self.feature_title,
            description=self.feature_description,
            target_date=self.feature_target_date,
            ticket_url=self.feature_ticket_url,
            product_area=self.feature_product_area,
            priority=1
        )
        feature2.save()
        feature3 = Feature(
            title=self.feature_title,
            description=self.feature_description,
            target_date=self.feature_target_date,
            ticket_url=self.feature_ticket_url,
            product_area=self.feature_product_area,
            priority=2
        )
        feature3.save()
        self.assertEqual(Feature.objects.get(pk=self.feature.pk).priority, 3)



class FeatureViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username="TheBestGeekInTheWorld")
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.feature_data = {
            'title': 'Feature view title test',
            'description': 'Description of the Feature request',
            'target_date': "2018-08-21",
            'ticket_url': 'http://www.example.com',
            'product_area': 'P',
            'priority': 1,
            'owner': user.id
        }
        self.response_post = self.client.post(
            reverse('features:list_create'),
            self.feature_data,
            format='json'
        )
        self.response_get = self.client.get(
            reverse('features:list_create'),
            format='json'
        )

    def test_authentication_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()

        # Unauthenticated user can do GET
        res_get = new_client.get(reverse('features:list_create'), format="json")
        self.assertEqual(res_get.status_code, status.HTTP_200_OK)

        # Unauthenticated user cannot post
        res_post = new_client.post(reverse('features:list_create'), format="json")
        self.assertEqual(res_post.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_create_feature(self):
        self.assertEqual(self.response_post.status_code, status.HTTP_201_CREATED)

    def test_api_create_feature_content(self):
        self.assertEqual(self.response_post.data["description"], self.feature_data['description'])
        self.assertEqual(self.response_post.data["product_area"], self.feature_data['product_area'])

    def test_api_get_features(self):
        self.assertEqual(self.response_get.status_code, status.HTTP_200_OK)

    def test_api_get_features_body(self):
        self.client.post(
            reverse('features:list_create'),
            self.feature_data,
            format='json'
        )
        response_get_all = self.client.get(
            reverse('features:list_create'),
            format='json'
        )
        self.assertEqual(len(response_get_all.data), 2)
        self.assertEqual(response_get_all.data[1]['id'], 2)

    def test_api_can_get_a_feature(self):
        """Test the api can get a given feature."""
        feature = Feature.objects.get()
        response = self.client.get(
            reverse('features:details', kwargs={'pk': feature.id}),
            format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, feature.title)

    def test_api_can_update_feature(self):
        """Test the api can update a given feature."""
        feature = Feature.objects.get()
        change_feature = {'title': 'something new'}
        res = self.client.put(
            reverse('features:details', kwargs={'pk': feature.pk}),
            change_feature, format='json'
        )
        self.assertEqual(res.json()['title'], change_feature['title'])
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_feature(self):
        """Test the api can delete a feature."""
        feature = Feature.objects.get()
        response = self.client.delete(
            reverse('features:details', kwargs={'pk': feature.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)