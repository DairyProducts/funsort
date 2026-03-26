def intelligent_design_sort(data, inPlace=False):
    """
    Sorts the list by the concept of intelligent design.

    As the list has already been consciously put into sorted order by an
    intelligent designer, this function simply returns the list as is.

    Time complexity: O(1) (best case), Ω(1) (worst case), Θ(1) (average case)

    Credit: David Morgan-Mar, dangermouse.net
    
    Args:
        data: A list to be sorted.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    result = data.copy()
    if inPlace:
        data[:] = result
        return data
    return result