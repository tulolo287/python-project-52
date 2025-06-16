from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

MIN_PASSWORD_LENGTH = 3


class UserCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
