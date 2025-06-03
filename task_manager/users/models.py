from django.contrib.auth.models import (
    User,
)


class User(User):
    def __repr__(self):
        return f"{self.__class__}"

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
