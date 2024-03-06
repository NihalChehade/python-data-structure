def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    sorted_list =sorted(ages)
    oldest_age=max(sorted_list)

    oldest_age_index= sorted_list.index(oldest_age)
    sorted_list.pop(oldest_age_index)

    second_oldest=max(sorted_list)

    while second_oldest==oldest_age:
        oldest_index=sorted_list.index(second_oldest)
        sorted_list.pop(oldest_index)
        second_oldest=max(sorted_list)
        
    return (second_oldest, oldest_age)

