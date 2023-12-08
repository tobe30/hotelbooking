from django import forms
from django.forms import DateTimeInput
from core.models import User, Booking

ADULT_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]

CHILDREN_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]

class BookingForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"firstname",'class': 'form-control'}),  required=True)
    lastname = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"E.g. Sina",'class': 'form-control'}),  required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Mobile",'class': 'form-control'}),  required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email",'class': 'form-control'}))
    adult = forms.ChoiceField(label='Adult', choices=ADULT_CHOICES, initial=0, widget=forms.Select(attrs={'class': 'custom-select'}))
    children = forms.ChoiceField(label='Children', choices=CHILDREN_CHOICES, initial=0, widget=forms.Select(attrs={'class': 'custom-select'}))
    checkin = forms.DateTimeField(label='Check-In', widget=DateTimeInput(attrs={'class': 'form-control', 'type':"date"}))
    checkout = forms.DateTimeField(label='Check-Out', widget=DateTimeInput(attrs={'class': 'form-control', 'type':"date"}))
    category = forms.CharField(widget=forms.HiddenInput())
    request = forms.CharField(label='Special Request', widget=forms.TextInput(attrs={"placeholder":"E.g. Special Request",'class': 'form-control'}))

    class Meta:
        model = Booking
        fields = ['firstname', 'lastname', 'phone', 'email', 'adult', 'children', 'checkin', 'checkout', 'category',
                  'request'] 