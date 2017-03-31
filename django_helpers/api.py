def get_pagination(request):
    """
    Return the pagination storage on the request if it exists, otherwise return an empty dict.
    
    :param request: 
    :return: 
    """
    return getattr(request,  '_pagination', {})
