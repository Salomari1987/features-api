# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status

from rest_framework.test import APITestCase


class UserRegistrationAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = reverse("users:list_create")

    def test_user_registration(self):
        user_data = {
            "username": "nemo",
            "email": "nemo@nobody.com",
            "password": "123123",
            "confirm_password": "123123"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unique_username_validation(self):
        user_data_1 = {
            "username": "nemo",
            "email": "nemo@nobody.com",
            "password": "123123",
            "confirm_password": "123123"
        }
        response = self.client.post(self.url, user_data_1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user_data_2 = {
            "username": "nemo",
            "email": "nemo@nobody.com",
            "password": "123123",
            "confirm_password": "123123"
        }
        response = self.client.post(self.url, user_data_2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nonmatching_passowrdss(self):
        user_data = {
            "username": "nemo",
            "email": "nemo@nobody.com",
            "password": "123123",
            "confirm_password": "wrong"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
