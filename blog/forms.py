from django import forms
from blog.models import Publication
from mailings.forms import StyleFormMixin


class PublicationForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('name', 'description', 'image', 'publication_activ', 'counter')

