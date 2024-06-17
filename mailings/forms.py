from django import forms
from django.forms import BooleanField
from mailings.models import Mailing, MailingMessage, RecipientClient


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class MailingUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        # fields = '__all__'
        fields = ("first_date", "periodicity", "message", "clients")
        # exclude = ('name')


class MailingUpdateModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ("status",)


class MailingMessageUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ("theme", "body")


class RecipientClientUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = RecipientClient
        fields = ("email", "full_name", "comment")
