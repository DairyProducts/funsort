def bogo_sort(data, inPlace=False):
    """
    The classic inefficient sorting algorithm.

    Checks if the list is sorted, and if not, shuffles it randomly until it is.

    Time complexity: O(n!) (best case), Ω(∞) (worst case), Θ(n!) (average case)

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
    while working != sorted(working):
        random.shuffle(working)
    if inPlace:
        data[:] = working
        return data
    return working