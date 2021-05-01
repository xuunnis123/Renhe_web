from django import template
from ..models import Finance

register = template.Library()

@register.simple_tag
def total_list():
    return Finance.objects.count()