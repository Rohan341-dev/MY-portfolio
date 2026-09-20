from django import template

register = template.Library()


@register.filter(name='split')
def split_string(value, delimiter=','):
    """Split a comma-separated string into a list."""
    if not value:
        return []
    return [item.strip() for item in str(value).split(delimiter) if item.strip()]
