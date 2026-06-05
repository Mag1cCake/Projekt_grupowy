from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from manager.models import Position, TaskType, Task

class ModelTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.task_type = TaskType.objects.create(name="Bug")
        self.worker = get_user_model().objects.create_user(
            username="testworker",
            password="password123",
            position=self.position
        )

    def test_position_str(self):
        self.assertEqual(str(self.position), "Developer")

    def test_task_type_str(self):
        self.assertEqual(str(self.task_type), "Bug")

    def test_worker_creation(self):
        self.assertEqual(self.worker.username, "testworker")
        self.assertEqual(self.worker.position.name, "Developer")


class ViewTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="password123"
        )
        self.client.login(username="admin", password="password123")

    def test_dashboard_view(self):
        url = reverse("manager:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task_list_view(self):
        url = reverse("manager:task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_worker_list_view(self):
        url = reverse("manager:worker-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
