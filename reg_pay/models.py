from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorWidget
from django import forms

class Regpay(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    color_save = models.CharField(max_length=100, default="#0c854b66", null=True, blank=True)
    reg_name = models.CharField(max_length=30)
    reg_date = models.DateTimeField("Dates of payment")
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.reg_name

class Color_class(forms.ModelForm):
    class Meta:
        model = Regpay
        fields = ['user', 'color_save']
        widgets = {
            'color_save': ColorWidget(),
        }

