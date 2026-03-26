def merge_sort(data, inPlace=False):
    """
    Sorts the list using the merge sort algorithm.

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

    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def _merge_sort(values):
        if len(values) <= 1:
            return values
        mid = len(values) // 2
        left = _merge_sort(values[:mid])
        right = _merge_sort(values[mid:])
        return _merge(left, right)

    sorted_data = _merge_sort(data.copy())
    if inPlace:
        data[:] = sorted_data
        return data
    return sorted_data



