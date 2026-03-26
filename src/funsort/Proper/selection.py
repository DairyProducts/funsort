def selection_sort(data, inPlace=False):
    """
    Sorts the list using the selection sort algorithm.

    Time complexity: O(n^2) (best case), Ω(n^2) (worst case), Θ(n^2) (average case)

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

    for i in range(len(working)):
        min_index = i
        for j in range(i + 1, len(working)):
            if working[j] < working[min_index]:
                min_index = j
        working[i], working[min_index] = working[min_index], working[i]
    if inPlace:
        data[:] = working
        return data
    return working