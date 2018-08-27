from urllib.parse import urlencode
from django import template

register = template.Library()


@register.simple_tag()
def pagination(request, num_page):
    get = request.GET.copy()
    get['page'] = num_page
    return urlencode(get)
