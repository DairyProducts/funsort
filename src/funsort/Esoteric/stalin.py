def stalin_sort(data, inPlace=False):
    """
    Iterates through the list and removes any elements that are out of order,
    leaving a sorted list of the remaining elements.

    Time complexity: O(n) (best case), Ω(n) (worst case), Θ(n) (average case)

    Args:
        data: A list to be sorted.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    working = data if inPlace else data.copy()
    result = []
    if not working:
        if inPlace:
            data[:] = result
            return data
        return result
    current_max = working[0]
    for item in working:
        if item >= current_max:
            result.append(item)
            current_max = item
    if inPlace:
        data[:] = result
        return data
    return result
