from django.urls import reverse
from django.core import serializers
from rest_framework import status
from rest_framework.test import APITestCase

from backend.regularplans.tests.factories.regularplans import RegularPlansFactory
from backend.regularplans.serializers import RegularPlanSerializer
from backend.users.tests.factories.users import UserFactory

class CreateRegularPlanTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.data = RegularPlanSerializer(RegularPlansFactory(owner=self.user)).data

    def test_can_create_regular_plan_without_authentication(self):
        response = self.client.post(reverse('regularplans-list'), self.data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_can_create_regular_plan(self):
        self.client.login(username=self.user.username, password='password')
        response = self.client.post(reverse('regularplans-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ListRegularPlanTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.login(username=self.user.username, password='password')
        self.regularplans = RegularPlansFactory.create_batch(3, owner=self.user, publish=True)
        self.regularplans_publish_false = RegularPlansFactory.create_batch(3, owner=self.user, publish=False)

    def test_can_list_all_regular_plans(self):
        response = self.client.get(reverse('regularplans-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)
    
    def test_can_list_publish_true_regular_plans(self):
        url = reverse('regularplans-list')+'?publish=true'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)