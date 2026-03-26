def heap_sort(data, inPlace=False):
    """
    Sorts the list using the heap sort algorithm.

    Time complexity: O(n log n) (best case), Ω(n log n) (worst case), Θ(n log n) (average case)

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

    def _heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            _heapify(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        _heapify(working, n, i)

    for i in range(n - 1, 0, -1):
        working[i], working[0] = working[0], working[i]
        _heapify(working, i, 0)

    if inPlace:
        data[:] = working
        return data
    return working