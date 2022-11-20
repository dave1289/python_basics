def list_check(lst):
    results = []
    for itm in lst:
       results.append(isinstance(itm, list))
    response = True
    for bool in results:
        if not bool == True:
            response = False
        elif bool == True:
            response = True
    return response
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
