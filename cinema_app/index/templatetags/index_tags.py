from django import template
from index.models import *
register = template.Library()

@register.simple_tag()
def get_categories():
    category = Category.objects.all()
    return {'category': category,}
