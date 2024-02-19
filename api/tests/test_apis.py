from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Task, Executor


class CreateTaskTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.executor = Executor.objects.create(name="Executor")

    def test_success(self):
        payload = {
            "executor": self.executor.pk,
            "priority": 1,
            "title": "test_task",
            "comment" : "comment"
        }
        response = self.client.post(
            reverse("api:create"), payload, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_error(self):
        payload = {
        "executor": 1,
        "priority": 1,
        "title": "test_task",
        #нет поля comment
        }
        response = self.client.post(
            reverse("api:create"), payload, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateTaskTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.executor = Executor.objects.create(name='Executor')
        self.task = Task.objects.create(
            executor=self.executor,
            priority=1,
            title='title',
            comment='comment'
        )

    def test_success(self):
        payload = {
                "executor": 1,
                "priority": 1,
                "title": "test_task",
                "comment": "comment"
            }
        response = self.client.patch(
                reverse("api:update", kwargs={"pk": self.task.pk}), payload, format='json'
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_error_invalid_method(self):
        payload = {
                "executor": 1,
                "priority": 1,
                "title": "test_task",
                "comment": "comment"
            }
        response = self.client.post(
                reverse("api:update", kwargs={"pk": self.task.pk}), payload, format='json'
            )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class DestroyTaskTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.executor = Executor.objects.create(name='Executor')
        self.task = Task.objects.create(
            executor=self.executor,
            priority=1,
            title='title',
            comment='comment'
        )

    def success(self):
        response = self.client.delete(
                reverse("api:destroy", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)