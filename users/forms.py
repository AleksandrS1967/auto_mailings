from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms
from mailings.forms import StyleFormMixin


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "phone", "avatar", "country")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()


class RecoverPasswordForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
