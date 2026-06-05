from django.urls import path

from manager.views import (
    IndexView,
    WorkerListView,
    TaskListView,
    PositionListView,
    TaskTypeListView,
    WorkerDetailView,
    TaskDetailView,
    PositionDetailView,
    TaskTypeDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,
    SignUpView,
    )

app_name = "manager"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("task_types/", TaskTypeListView.as_view(), name="task-type-list"),

    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("task_types/<int:pk>/", TaskTypeDetailView.as_view(), name="task-type-detail"),

    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("task_types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),

    path ("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task_types/update/<int:pk>/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("positions/update/<int:pk>/", PositionUpdateView.as_view(), name="position-update"),
    path("workers/update/<int:pk>/", WorkerUpdateView.as_view(), name="worker-update"),

    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("task_types/delete/<int:pk>/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
    path("positions/delete/<int:pk>/", PositionDeleteView.as_view(), name="position-delete"),
    path("workers/delete/<int:pk>/", WorkerDeleteView.as_view(), name="worker-delete"),
]


