from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as translate


class CheckTaskMixin:
    error_message = translate(
        "You cannot delete a label which is currently being used."
    )

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_error_message)
        return redirect(self.success_url)
