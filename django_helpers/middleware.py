from django.conf import settings
from django.utils.deprecation import MiddleWareMixin

from . import constants


class PaginationMiddleware(MiddlewareMixin):
    """
    Middleware that handles pagination parameters
    """

    def process_request(self, request):
        pagination = {
            'filters': {},
            'sort': None,
            'direction': None,
            'search': None,
            'page': 1
        }

        if request.POST and 'search' in request.POST:
            pagination['search'] = request.POST.get('search')
        elif 'search' in request.GET:
            pagination['search'] = request.GET.get('search')

        if 'page' in request.GET:
            try:
                pagination['page'] = int(request.GET.get('page'))
            except ValueError:
                pass

        if 'filters' in request.GET:
            for word in request.GET.get('filters').split(','):
                filter_key, filter_value = word.split(':')
                pagination['filters'][filter_key] = filter_value

        if 'direction' in request.GET and 'sort' in request.GET:
            pagination['direction'] = request.GET.get('direction')
            pagination['sort'] = request.GET.get('sort')

        request._pagination = pagination

    def process_response(self, request, response):
        if hasattr(request, '_paginator') and hasattr(request, '_results'):
            pagination = request._pagination
            paginator = request._paginator
            results = request._results

            if hasattr(settings, 'PAGINATOR_RANGE_OFFSET'):
                range_offset = settings.PAGINATOR_RANGE_OFFSET
            else:
                range_offset = constants.PAGINATOR_RANGE_OFFSET

            range_start = pagination['page'] - range_offset
            range_start = range_start if range_start >= 1 else 1

            range_end = pagination['page'] + range_offset
            range_end = range_end if range_end <= paginator.num_pages else paginator.num_pages

            pagination['pages'] = {
                'current': pagination['page'],
                'last': paginator.num_pages,
                'first': 1,
                'range_start': range_start if range_start >= 1 else 1,
                'range_end': range_end if range_end <= paginator.num_pages else paginator.num_pages,
                'range': range(range_start, range_end + 1),
                'has_next': results.has_next,
                'has_previous': results.has_previous,
                'previous_page_number': results.previous_page_number,
                'next_page_number': results.next_page_number
            }

            request._pagination = pagination
            del request._paginator
            del request._results

        return response
