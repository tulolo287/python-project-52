from django.urls import path

from .views import (
    IndexLabelView,
    CreateLabelView,
    UpdateLabelView,
    DeleteLabelView,
)

urlpatterns = [
    path("", IndexLabelView.as_view(), name="labels"),
    path("create/", CreateLabelView.as_view(), name="label_create"),
    path("<int:pk>/update/", UpdateLabelView.as_view(), name="label_update"),
    path("<int:pk>/delete/", DeleteLabelView.as_view(), name="label_delete"),
]
