from django import forms
from .models import Category, MyDebts, OthersDebts, Currency
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError

CURRENCIES = [('UAN', 'UAN'), ('USD', 'USD'), ('EUR', 'EUR')]


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name', 'the_limit', 'currently_spent', 'date_of_rent', 'due_date', 'color_save']
        widgets = {
            'cat_name': forms.TextInput(attrs={'placeholder': 'Enter category name', 'class': 'input-text'}),
            'the_limit': forms.NumberInput(attrs={'placeholder': '0', 'class':'input-text', 'type':"text", 'id':"limit"}),
            'currently_spent': forms.NumberInput(attrs={'placeholder': '0', 'class':"input-text", 'type':"text", 'id':"spent"}),
            'date_of_rent': forms.DateInput(attrs={'type': 'date','id':'start-date', 'class': 'input-text'}),
            'due_date': forms.DateInput(attrs={'type': 'date','id':'end-date', 'class': 'input-text'}),
            'currency': forms.Select(choices=CURRENCIES, attrs={'class': 'custom-dropdown', 'id':'currency'}),
            'color_save': forms.TextInput(attrs={'type':"color", 'id':"bg-color", 'style':"width: 3px; height: 3px; border-radius: 360px"})
        }

    def clean_date_of_rent(self):
       data = self.cleaned_data['date_of_rent']
       if data < datetime.date.today():
            raise ValidationError(('Invalid date - impossible to create until today'))
       return data
    
    def clean_due_date(self):
       data = self.cleaned_data['due_date']
       if data < datetime.date.today():
            raise ValidationError(('Invalid date - impossible to create due today'))
       return data

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  
        super(CategoryCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CategoryCreateForm, self).clean()
        cleaned_data['user'] = self.request.user  
        return cleaned_data
    

class MyDebtsCreateForm(forms.ModelForm):
    class Meta:
        model = MyDebts
        fields = ['debt_amount', 'currency', 'date_of_borrowing', 'debt_repayment_date', 'creditor_name']
        widgets = {
            'debt_amount': forms.NumberInput(attrs={'placeholder': 'Enter debt amount'}),
            'currency': forms.Select(choices=Currency.choices, attrs={'class': 'custom-dropdown', 'id':'currency'}),
            'date_of_borrowing': forms.DateInput(attrs={'type': 'date'}),
            'debt_repayment_date': forms.DateInput(attrs={'type': 'date'}),
            'creditor_name': forms.TextInput(attrs={'placeholder': 'Enter creditors name'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MyDebtsCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(MyDebtsCreateForm, self).clean()
        cleaned_data['user'] = self.request.user
        return cleaned_data


class OthersDebtsCreateForm(forms.ModelForm):
    class Meta:
        model = OthersDebts
        fields = ['debt_amount', 'currency', 'date_of_borrowing', 'debt_repayment_date', 'debtor_name']
        widgets = {
            'debt_amount': forms.NumberInput(attrs={'placeholder': '0'}),
            'currency': forms.Select(choices=Currency.choices, attrs={'class': 'custom-dropdown', 'id': 'currency'}),
            'date_of_borrowing': forms.DateInput(attrs={'type': 'date'}),
            'debt_repayment_date': forms.DateInput(attrs={'type': 'date'}),
            'creditor_name': forms.TextInput(attrs={'placeholder': 'Enter creditors name'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OthersDebtsCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(OthersDebtsCreateForm, self).clean()
        cleaned_data['user'] = self.request.user
        return cleaned_data