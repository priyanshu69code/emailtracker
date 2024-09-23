from django import template

register = template.Library()

@register.filter
def get_field_value(instance, field_name):
    """Returns the value of a field by its name from a model instance."""
    return getattr(instance, field_name, None)
