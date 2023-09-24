from django import forms
from .models import ServerProperties


class ServerPropertiesForm(forms.ModelForm):
    class Meta:
        model = ServerProperties
        fields = "__all__"
