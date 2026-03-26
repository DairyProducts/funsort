def thanos_sort(data, inPlace=False):
    """
    Sorts the list in a way that is inevitable.

    Thanos snaps his fingers and removes half of the elements in the list.
    He continues to do so until one final (sorted) element remains, or until
    the list is otherwise sorted. The final list is perfectly balanced,
    as all things should be.

    Time complexity: O(n) (best case), Ω(n) (worst case), Θ(n) (average case)

    Credit: Mohit Srinivasan, https://github.com/atomisadev/thanos-sort

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
    while len(working) > 1:
        working = working[::2]
        if working == sorted(working):
            if inPlace:
                data[:] = working
                return data
            return working
    if inPlace:
        data[:] = working
        return data
    return working