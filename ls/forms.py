from django import forms
from .models import Sale, Customer, User
from django.forms import DateTimeInput

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User




class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 
                  'surname', 
                  'email', 
                  'phone', 
                  'dt_of_reg', 
                  'percent_of_discount', 
                  'current_balance', 
                #   'next_level', 
                  'shop',
                #   'money_spent_cus',
        )
        widgets = {
            'dt_of_reg': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'percent_of_discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_balance': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'next_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'shop': forms.Select(attrs={'class': 'form-control'}), # Используем виджет Select
            # 'money_spent_cus': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(CustomerModelForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True


class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('purchase_amount',
                  'accumulated_bonuses', 
                  'the_number_of_bonuses_to_be_debited', 
                  'sum_of_purchase',

                  'percent_of_discount', 
                  'customer', 
                  'current_balance',


                  'dt_of_sale', 
                  'shop',
        )
        widgets = {
            'dt_of_sale': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
            
        }



class LoginForm(forms.Form):
    username = forms.CharField(label='Name', 
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'input-control'}))
    
    
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'input-control'}))


class CustomerSearchForm(forms.Form):
    search_query = forms.CharField(label='Find a customer by the phone', required=False)

