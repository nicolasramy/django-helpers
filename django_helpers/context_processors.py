from django_helpers.api import get_pagination


def pagination(request):
    """
    Return a lazy 'pagination' context variable
    
    :param request: 
    :return: dict 
    """

    return {
        'pagination': get_pagination(request)
    }
