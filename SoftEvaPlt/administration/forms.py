from django import forms
from django.forms.widgets import Input

class IndicatorForm(forms.Form):
    si_id = forms.IntegerField(label = '安全指标ID')
    si_category = forms.CharField(label = '指标分类', max_length = 30, widget = Input)
    si_name = forms.CharField(label = '安全指标名称', max_length = 30, widget = Input)
    si_state = forms.IntegerField(label = '安全指标状态')
    si_creator = forms.CharField(label = '安全指标创建人', max_length = 30)
    si_create_time = forms.DateTimeField(label = '安全指标创建时间')