from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class HotelDetailsFrom(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    place = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))