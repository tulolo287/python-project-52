from django import (
    forms,
)

from task_manager.users.models import (
    User,
)


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"title": "Password must contains at least 3 chars"}
        ),
    )
    password_confirm = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                "title": "Please, type your password again",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
        )
        # "__all__"   ['name', 'second_name', 'username']

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(
            *args,
            **kwargs,
        )

        for field in self.fields.values():
            field.widget.attrs["placeholder"] = field.label
            field.widget.attrs["class"] = "form-control"

    def save(
        self,
        commit=True,
    ):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
