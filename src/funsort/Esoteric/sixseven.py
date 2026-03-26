def six_seven_sort(data, inPlace=False):
    """
    Sorts the list in a manner that will make you lose faith in humanity.

    Removes all elements from the list except for 6 and 7, and sorts what is left.

    Time complexity: O(n) (best case), Ω(n) (worst case), Θ(n) (average case)

    Credit: @swapjs.ig on Instagram

    Args:
        data: A list to be sorted.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in the list must be int or float")
    working = data if inPlace else data.copy()
    filtered = [x for x in working if x == 6 or x == 7]
    result = sorted(filtered)
    if inPlace:
        data[:] = result
        return data
    return result