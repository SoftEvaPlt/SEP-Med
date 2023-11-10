from django import forms
from .models import Task

# 传入product_TD
class product_TD_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['product_td']

# 传入product_AD
class product_TD_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['product_ad']