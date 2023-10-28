from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorWidget
from django import forms

class Currency(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=30)
    the_limit = models.IntegerField(default=0)
    currently_spent = models.IntegerField(default=0)
    date_of_rent = models.DateTimeField("Date of rent")
    due_date = models.DateTimeField("Due date")
    currency = models.ForeignKey(to=Currency, on_delete=models.SET_NULL, null=True, blank=True)
    color_save = models.CharField(max_length=9, default="#0c854b66", null=True, blank=True)


    def __str__(self):
        return self.currency if self.currency else 'No Currency'


class Color_class(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['user', 'color_save']
        widgets = {
            'color_save': ColorWidget(),
        }



