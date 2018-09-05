from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import CATEGORIES, CONDITIONS


class AdSearchFrom(forms.Form):
    query = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'search-input',
            'placeholder': _('What are you looking for?')
        })
    )
    location = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'search-location',
            'placeholder': _('Location')
        })
    )
    condition = forms.ChoiceField(
        choices=CONDITIONS,
        required=False,
        widget=forms.Select(attrs={
            'class': 'condition'
        })
    )
    price_from = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'price',
            'placeholder': _('Price from'),
            'min': '0'
        })
    )
    price_to = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'price',
            'placeholder': _('Price to'),
            'min': '0'
        })
    )
    image_only = forms.BooleanField(
        label=_('Only with a photo'),
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox'
        })
    )


class AdForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': _('Title')
        })
    )
    category = forms.ChoiceField(
        choices=CATEGORIES,
        widget=forms.Select(attrs={
            'class': 'choices-list'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'text_area'
        })
    )
    condition = forms.ChoiceField(
        choices=CONDITIONS,
        widget=forms.Select(attrs={
            'class': 'choices-list'
        })
    )
    photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'id': 'photo',
            'class': 'photo'
        })
    )
    photo2 = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'id': 'photo2',
            'class': 'photo'
        })
    )
    photo3 = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'id': 'photo3',
            'class': 'photo'
        })
    )
    photo4 = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'id': 'photo4',
            'class': 'photo'
        })
    )
    location = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': _('Location')
        })
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'text_input'
        })
    )
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'text_input tel'
        })
    )
