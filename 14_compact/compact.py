def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    truthy_values_list = []
    for value in lst:
        if not not value:
            truthy_values_list.append(value)
    return truthy_values_list

    