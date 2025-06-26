from django.urls import path

from .views import (
    TaskIndexView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDetail,
)

urlpatterns = [
    path("", TaskIndexView.as_view(), name="tasks"),
    path("<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]
