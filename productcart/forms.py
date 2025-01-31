from dataclasses import field
from logging import PlaceHolder
from django import forms

from .models import Checkout

class CheckoutForm(forms.ModelForm):
    PAYMENT_CHOICES = [
        ('payment_on_delivery', 'Payment on Delivery'),
        ('card', 'Credit/Debit Card'),
    ]
    
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'w-5 h-5 border border-gray-300 rounded bg-transparent focus:outline-none focus:ring-1'})
    )
    
    save_info = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'w-5 h-5 border border-gray-300 rounded bg-transparent focus:outline-none focus:ring-1'})
    )
    
    terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'w-5 h-5 border border-gray-300 rounded bg-transparent focus:outline-none focus:ring-1'})
    )

    class Meta:
        model = Checkout
        fields = ['firstname', 'lastname', 'email', 'address', 'city', 'state', 'phone_number']
        widgets = {
            'firstname': forms.TextInput(attrs={
                'class': 'w-full text-sm border border-gray-300 rounded bg-transparent lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600 py-3',
                'placeholder': 'First Name'
            }),
            'lastname': forms.TextInput(attrs={
                'class': 'w-full text-sm border border-gray-300 rounded bg-transparent lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600 py-3',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 text-sm border border-gray-300 rounded bg-transparent lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600',
                'placeholder': 'Email'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 text-xs border border-gray-300 rounded bg-transparent lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600',
                'rows': 4,
                'placeholder': 'House number and Street name'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 text-sm border border-gray-300 rounded bg-transparent lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600',
                'placeholder': 'City'
            }),
            'state': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 text-sm border border-gray-300 rounded bg-transparent lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600',
                'placeholder': 'State'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 text-sm border border-gray-300 rounded bg-transparent lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600',
                'placeholder': 'Phone Number'
            }),
        }
