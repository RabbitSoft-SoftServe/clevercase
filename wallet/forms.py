from django import forms
from .models import Category, Color_class
from django.contrib.auth.models import User

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name', 'the_limit', 'currently_spent', 'date_of_rent', 'due_date', 'currency']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Извлекаем 'request' из kwargs
        super(CategoryCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CategoryCreateForm, self).clean()
        cleaned_data['user'] = self.request.user  # Устанавливаем 'user' в cleaned_data
        return cleaned_data