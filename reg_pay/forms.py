from django import forms
from .models import Regpay



class RegpayCreateForm(forms.ModelForm):
    class Meta:
        model = Regpay
        fields = ['reg_name', 'reg_date', 'reg_name', 'amount', 'color_save']
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RegpayCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(RegpayCreateForm, self).clean()
        cleaned_data['user'] = self.request.user
        return cleaned_data