def schrodinger_sort(data, inPlace=False):
    """
    Sorts the list by the concept of Schrodinger's cat.

    The output list is considered to be both sorted and unsorted until it is observed.

    Time complexity: O(n) (best case), Ω(n log n) (worst case), Θ(n log n) (average case)

    Args:
        data: A list to be sorted.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    import random
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    working = data if inPlace else data.copy()
    if random.choice([True, False]):
        result = sorted(working)
    else:
        result = working.copy()
    if inPlace:
        data[:] = result
        return data
    return result