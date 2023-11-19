from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorWidget
from django import forms
import datetime
from django.utils import timezone
class Currency(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=30)
    the_limit = models.IntegerField(default=0)
    currently_spent = models.IntegerField(default=0)
    date_of_rent = models.DateField("Date of rent", default=timezone.now)
    due_date = models.DateField("Due date")
    currency = models.CharField(max_length=30)
    color_save = models.CharField(default="#0c854b66", max_length=100, blank=False)


    def __str__(self):
        return self.cat_name 


class Color_class(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['user', 'color_save']
        widgets = {
            'color_save': ColorWidget(),
        }



