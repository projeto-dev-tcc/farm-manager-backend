from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_groups')
def has_groups(user, groups_names):
    return user.groups.filter(name__in=groups_names.split("|")).exists()
