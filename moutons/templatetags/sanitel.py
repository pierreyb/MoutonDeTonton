from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

@register.filter(is_safe=True)
@stringfilter
def sanitel(value):
    sanitel_output_format = ''
    if len(value) > 0:
        sanitel_output_format = '{}--{}'.format(value[0:len(value) - 4], value[len(value) - 4:])
    return sanitel_output_format