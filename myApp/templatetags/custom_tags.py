from django import template

register = template.Library()

@register.filter
def zip_lists(a, b):
    return zip(a, b)

@register.filter
def my_custom_filter(value):
    # Your custom filter logic here
    pass


@register.filter
def div(value,arg):
    try:
        return int(value)/int(arg)
    except(ValueError,ZeroDivisionError):
        return None

@register.filter
def mul(value,arg):
    try:
        return int(value)*int(arg)
    except(ValueError,ZeroDivisionError):
        return None
    