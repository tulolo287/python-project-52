from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"{self.__class__}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
