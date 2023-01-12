from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User, Account, UserProfile
from django.forms import ModelForm
from django_countries.fields import CountryField


# Profile account forms

class AccountForm(ModelForm):
    """User account form to edit base information """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number']


class ImageForm(ModelForm):
    """Image form to update profile picture"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = UserProfile
        fields = ['profile_picture']


class AddressForm(ModelForm):
    """Address form to change shipping information"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['street_address2'].required = False
        self.fields['county'].required = False
        self.fields['postcode'].required = False

    street_address1 = forms.CharField(max_length=100)
    street_address2 = forms.CharField(max_length=100)
    town_or_city = forms.CharField(max_length=30)
    county = forms.CharField(max_length=30)
    postcode = forms.CharField(max_length=30)
    country = CountryField(max_length=5)

    class Meta:
        model = UserProfile
        fields = ['street_address1', 'street_address2', 'town_or_city',
                  'county', 'postcode', 'country']
