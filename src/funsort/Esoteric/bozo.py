def bozo_sort(data, inPlace=False):
    """
    A little bit more efficient than Bogosort, but still not a good sorting algorithm.

    Checks if the list is sorted, and if not, randomly swaps two elements until it is.

    Time complexity: O(n^2) (best case), Ω(∞) (worst case), Θ(n^2) (average case)

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
        i, j = random.sample(range(len(working)), 2)
        working[i], working[j] = working[j], working[i]
    if inPlace:
        data[:] = working
        return data
    return working