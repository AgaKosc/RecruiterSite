from django import template
from django.forms.fields import CheckboxInput
from django.forms.widgets import CheckboxSelectMultiple

register = template.Library()

@register.filter(name='is_checkbox')
def is_checkbox(value):
    return isinstance(value, CheckboxInput)

@register.filter(name='is_checkbox_select_multiple')
def is_checkbox_select_multiple(value):
    return isinstance(value, CheckboxSelectMultiple)