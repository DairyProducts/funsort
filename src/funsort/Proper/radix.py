def radix_sort(data, inPlace=False):
    """
    Sorts the list using the radix sort algorithm.

    Only works for non-negative `int` values.

    Time complexity: O(n * k) (best case), Ω(n * k) (worst case), Θ(n * k) (average case)
    where k is the number of digits in the largest number.

    Args:
        data: A list to be sorted. All elements must be non-negative integers.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    if (not all(isinstance(x, int) for x in data)) or (not all(x >= 0 for x in data)):
        raise TypeError("All elements in the list must be non-negative integers")
    
    working = data if inPlace else data.copy()

    if len(working) == 0:
        return data if inPlace else working

    max_num = max(working)
    exp = 1
    
    while max_num // exp > 0:
        count = [0] * 10
        output = [0] * len(working)
        for i in range(len(working)):
            index = (working[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(len(working) - 1, -1, -1):
            index = (working[i] // exp) % 10
            output[count[index] - 1] = working[i]
            count[index] -= 1
        for i in range(len(working)):
            working[i] = output[i]
        exp *= 10
    if inPlace:
        data[:] = working
        return data
    return working