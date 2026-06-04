from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Task, TaskType, Worker, Position


class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "deadline", "priority", "is_completed", "task_type"]
    search_fields = ("name",)
    list_filter = ("is_completed", "priority")
    filter_horizontal = ("assignees",)

admin.site.register(Task, TaskAdmin)


class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name",)

admin.site.register(TaskType, TaskTypeAdmin)


class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )
    search_fields = ("username", "first_name", "last_name")
    list_filter = ("position",)

admin.site.register(Worker, WorkerAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name",)

admin.site.register(Position, PositionAdmin)
