from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm, WorkerCreateForm, WorkerUpdateForm
from manager.models import Task, Worker, Position, TaskType


class IndexView(generic.TemplateView):
    template_name = "manager/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_tasks"] = Task.objects.count()
        context["num_workers"] = Worker.objects.count()
        return context


class SignUpView(generic.CreateView):
    form_class = WorkerCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

"""List views"""
class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "manager/task_type_list.html"


"""Detail views"""
class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "manager/task_detail.html"


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position
    template_name = "manager/position_detail.html"


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
    context_object_name = "task_type"


"""Create views"""
class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_form.html"


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")
    template_name = "manager/position_form.html"


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("manager:index")
    template_name = "manager/worker_form.html"


"""Update views"""
class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_form.html"


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")
    template_name = "manager/position_form.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("manager:worker-list")
    template_name = "manager/worker_form.html"


"""Delete views"""
class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_confirm_delete.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_confirm_delete.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("manager:position-list")
    template_name = "manager/position_confirm_delete.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:index")
    template_name = "manager/worker_confirm_delete.html"
