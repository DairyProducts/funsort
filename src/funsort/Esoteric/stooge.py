def stooge_sort(data, l=0, h=None, inPlace=False):
    """
    A cutting-edge and brilliantly formulated sorting algorithm that is known for its
    remarkably and exceptionally poor performance.

    Time complexity: O(n^2.7095) (best case), Ω(n^2.7095) (worst case), Θ(n^2.7095) (average case)

    Args:
        data: A list to be sorted.
        l: Starting index of the segment to sort.
        h: Ending index of the segment to sort.

    Returns:
        The sorted list.
    """
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    working = data if inPlace else data.copy()

    if h is None:
        h = len(working) - 1

    def _stooge(arr, left, right):
        if left >= right:
            return
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if right - left + 1 > 2:
            third = (right - left + 1) // 3
            _stooge(arr, left, right - third)
            _stooge(arr, left + third, right)
            _stooge(arr, left, right - third)

    _stooge(working, l, h)
    if inPlace:
        data[:] = working
        return data
    return working