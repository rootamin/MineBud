from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Player


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = Player
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Player.objects.filter(email=email).exists():
            raise forms.ValidationError("This Email address is already registered.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['username', 'email']