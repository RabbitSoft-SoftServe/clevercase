from django import forms
from .models import Category, Color_class
from django.contrib.auth.models import User

CURRENCIES = [('UAN', 'UAN'), ('USD', 'USD'), ('EUR', 'EUR')]


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name', 'the_limit', 'currently_spent', 'date_of_rent', 'due_date', 'currency', 'color_save']
        widgets = {
            'cat_name': forms.TextInput(attrs={'placeholder': 'Enter category name', 'class': 'input-text'}),
            'the_limit': forms.NumberInput(attrs={'placeholder': '0', 'class':'input-text', 'type':"text", 'id':"limit"}),
            'currently_spent': forms.NumberInput(attrs={'placeholder': '0', 'class':"input-text", 'type':"text", 'id':"spent"}),
            'date_of_rent': forms.DateInput(attrs={'type': 'date','id':'start-date', 'class': 'input-text'}),
            'due_date': forms.DateInput(attrs={'type': 'date','id':'end-date', 'class': 'input-text'}),
            'currency': forms.Select(choices=CURRENCIES, attrs={'class': 'custom-dropdown', 'id':'currency'}),
            'color_save': forms.TextInput(attrs={'type':"color", 'id':"bg-color", 'style':"width: 3px; height: 3px; border-radius: 360px"})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  
        super(CategoryCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CategoryCreateForm, self).clean()
        cleaned_data['user'] = self.request.user  
        return cleaned_data