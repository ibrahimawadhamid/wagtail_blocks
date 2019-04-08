"""
  When editing the content use the brackets:
  [[ <iframe>..</iframe> ]]
  And after, use it in templates like this:
  {{ page.body|resolve_html|richtext }}
"""
from django import template

register = template.Library()


@register.filter
def resolve_html(value):
    temp = str(value).splitlines()
    new_string = ''.join([str(x) for x in temp])
    new = new_string.replace('<p>[[', '')
    new = new.replace(']]</p>', '')
    new = new.replace('&lt;', '<')
    new = new.replace('&gt;', '>')
    return new
