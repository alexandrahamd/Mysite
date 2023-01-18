from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def mediapath(text, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '/media/%s' % (esc(text))
    return mark_safe(result)


@register.simple_tag
def mediapath(text):
    return '/media/%s' % text
