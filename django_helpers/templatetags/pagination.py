from django import template
from django.utils.http import urlquote

register = template.Library()


@register.filter
def pagination_nav_url(data, page):
    if page == data['pages']['current']:
        return '#'
    else:
        url = '?page=%d' % page

    if data['filters']:
        serialized_filters = list()
        for filter_key in data['filters']:
            serialized_filters.append('%s:%s' % (filter_key, data['filters'][filter_key]))

        if len(serialized_filters):
            url += '&filters=%s' % '+'.join(serialized_filters)

    if data['direction']:
        url += '&direction=%s' % data['direction']

    if data['sort']:
        url += '&sort=%s' % data['sort']

    if data['search']:
        url += '&search=%s' % urlquote(data['search'])

    return url


@register.filter
def pagination_filter_url(data, filters):

    current_filter_key, current_filter_value = filters.split(':')

    url = '?filters=%s' % filters

    if data['filters']:
        for filter_key in data['filters']:
            if filter_key == current_filter_key:
                continue
            url += ',%s:%s' % (filter_key, data['filters'][filter_key])

    if data['direction']:
        url += '&direction=%s' % data['direction']

    if data['sort']:
        url += '&sort=%s' % data['sort']

    if data['search']:
        url += '&search=%s' % urlquote(data['search'])

    return url
