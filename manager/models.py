from django.contrib.auth.models import AbstractUser
from django.db import models


class Worker(AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True)
    position = models.ForeignKey("Position", on_delete=models.SET_NULL, related_name="workers", null=True, blank=True)

    def __str__(self) -> str:
        return f"Worker: {self.username}({self.first_name} {self.last_name}) -> {self.position}"


class Position(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("urgent", "Urgent"),
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    is_completed = models.BooleanField(default=False, null=False, blank=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    task_type = models.ForeignKey("TaskType", on_delete=models.SET_NULL, related_name="tasks", null=True, blank=True)
    assignees = models.ManyToManyField("Worker", related_name="assignees", blank=True)

    def __str__(self) -> str:
        return (
            f"Task: {self.name}\n"
                f" Description: {self.description}\n"
                f" Priority: {self.priority}\n"
                f" Task Type: {self.task_type}"
        )


class TaskType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
