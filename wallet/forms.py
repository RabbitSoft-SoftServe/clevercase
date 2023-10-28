from django import forms
from .models import Category, Color_class


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
