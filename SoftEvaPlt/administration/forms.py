from django import forms
from django.forms.widgets import Input

class IndicatorForm(forms.Form):
    si_id = forms.IntegerField(label = '安全指标ID')
    si_category = forms.CharField(label = '指标分类', max_length = 30, widget = Input)
    si_name = forms.CharField(label = '安全指标名称', max_length = 30, widget = Input)
    si_state = forms.IntegerField(label = '安全指标状态')
    si_creator = forms.CharField(label = '安全指标创建人', max_length = 30)
    si_create_time = forms.DateTimeField(label = '安全指标创建时间')

class SceneForm(forms.Form):
    scene_id = forms.IntegerField(label='场景ID')
    scene_name = forms.CharField(label='场景名称', max_length=30, widget = Input)
    scene_state = forms.IntegerField(label='场景状态')
    scene_description = forms.CharField(label='场景描述', max_length=200, widget = Input)
    scene_creator = forms.CharField(label='场景创建人', max_length=30)
    scene_create_time = forms.DateTimeField(label='场景创建时间')