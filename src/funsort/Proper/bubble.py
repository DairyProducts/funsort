def bubble_sort(data, inPlace=False):
    """
    Sorts the list using the bubble sort algorithm.

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
    n = len(working)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if working[j] > working[j + 1]:
                working[j], working[j + 1] = working[j + 1], working[j]
                swapped = True
        if not swapped:
            break
    if inPlace:
        data[:] = working
        return data
    return working
