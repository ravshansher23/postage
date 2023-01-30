from django import forms
from django.utils.translation import gettext_lazy as _
from mainapp import models as mainapp_models

class MailForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput)
    countdown = forms.NumberInput()


