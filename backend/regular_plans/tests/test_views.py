from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from backend.regular_plans.serializers import RegularPlanSerializer
from backend.regular_plans.tests.factories.regular_plans import (
    RegularPlansFactory,
    UserFactory,
)


class RegularPlanViewSetTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.regular_plans = RegularPlansFactory.create_batch(
            3, owner=self.user, publish=True
        )
        self.regular_plans_publish_false = RegularPlansFactory.create_batch(
            3, owner=self.user, publish=False
        )
        self.data = RegularPlanSerializer(self.regular_plans[0]).data
        self.client.login(username=self.user.username, password="password")
        self.url = reverse("regular-plans-list")

    def test_can_list_all_regular_plans(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_can_list_publish_true_regular_plans(self):
        url = self.url + "?publish=true"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_can_create_regular_plan(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_update_regular_plan(self):
        data = self.data
        data.name = "New Name"
        url = reverse("regular-plans-detail", kwargs={"pk": self.data["id"]})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(url)
        self.assertEqual(response.data["name"], data["name"])

    def test_can_delete_regular_plan(self):
        url = reverse("regular-plans-detail", kwargs={"pk": self.data["id"]})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_cant_create_regular_plan_without_authentication(self):
        self.client.logout()
        response = self.client.post(self.url, self.data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
