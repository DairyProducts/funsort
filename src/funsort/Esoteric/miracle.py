def miracle_sort(data, wait_time=1.0, inPlace=False):
    """
    Sorts the list by praying for a miracle.

    Checks if the list is already sorted. If it is, it returns the list as is.
    If not, waits for a miracle, and then checks again.

    Time complexity: O(n) (best case), Ω(∞) (worst case), Θ(∞) (average case)

    Credit: Ryan Okushi, https://pages.cs.wisc.edu/~okushi/

    Args:
        data: A list to be sorted.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    import time
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    working = data if inPlace else data.copy()
    if working != sorted(working):
        time.sleep(wait_time)
    result = sorted(working)
    if inPlace:
        data[:] = result
        return data
    return result