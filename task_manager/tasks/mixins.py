from django.contrib import messages

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as translate


class AuthorRequireMixin(UserPassesTestMixin):
    author_require_message = translate("Only author has permission")

    def test_func(self):
        return self.get_object().author.id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, self.author_require_message)
        return redirect(self.success_url)
