def quick_sort(data, inPlace=False):
    """
    Sorts the list using the quick sort algorithm.

    The pivot is chosen as the middle element of the list.

    Time complexity: O(n log n) (best case), Ω(n^2) (worst case), Θ(n log n) (average case)

    Args:
        data: A list to be sorted.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")

    def _quick_sort(values):
        if len(values) <= 1:
            return values
        pivot = values[len(values) // 2]
        left = [x for x in values if x < pivot]
        middle = [x for x in values if x == pivot]
        right = [x for x in values if x > pivot]
        return _quick_sort(left) + middle + _quick_sort(right)

    sorted_data = _quick_sort(data.copy())
    if inPlace:
        data[:] = sorted_data
        return data
    return sorted_data
