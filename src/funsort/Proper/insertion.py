def insertion_sort(data, inPlace=False):
    """
    Sorts the list using the insertion sort algorithm.

    Time complexity: O(n) (best case), Ω(n^2) (worst case), Θ(n^2) (average case)

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

    for i in range(1, len(working)):
        key = working[i]
        j = i - 1
        while j >= 0 and working[j] > key:
            working[j + 1] = working[j]
            j -= 1
        working[j + 1] = key

    if inPlace:
        data[:] = working
        return data
    return working