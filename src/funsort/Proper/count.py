def counting_sort(data, inPlace=False):
    """
    Sorts the list using the counting sort algorithm.

    Only works for int values.

    Time complexity: O(n + k) (best case), Ω(n + k) (worst case), Θ(n + k) (average case)
    where k is the range of the input values.

    Args:
        data: A list to be sorted. All elements must be integers.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    if not all(isinstance(x, int) for x in data):
        raise TypeError("All elements in the list must be integers")
    if not data:
        return data if inPlace else []
    max_val = max(data)
    min_val = min(data)
    count_range = max_val - min_val + 1
    count = [0] * count_range
    for num in data:
        count[num - min_val] += 1
    sorted_data = []
    for i, c in enumerate(count):
        sorted_data.extend([i + min_val] * c)
    if inPlace:
        data[:] = sorted_data
        return data
    return sorted_data