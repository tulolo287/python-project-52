from django import forms
from django.utils.translation import gettext_lazy as translate

from .models import Label


class LabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': translate('name'),
                }
            )
        }
        labels = {'name': translate('Name')}
