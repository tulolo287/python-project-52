from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.urls import reverse_lazy as reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusIndexView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = "statuses"
    template_name = "statuses/index.html"

class StatusCreateView(LoginRequiredMixin, CreateView):
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = "statuses/create.html"
    success_url = reverse('statuses')

class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = "statuses/update.html"
    success_url = reverse('statuses')

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    context_object_name = "statuses"
    template_name = "statuses/delete.html"
    success_url = reverse('statuses')

