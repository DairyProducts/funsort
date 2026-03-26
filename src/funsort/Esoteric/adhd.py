def adhd_sort(data, inPlace=False):
    """
    In sorting the list, the interpreter keeps getting distracted...

    The interpreter also reports beings unable to focus on much, losing
    track of time, having difficulty organizing its belongings, among other
    symptoms. Maybe we should get it checked out.

    Time complexity: O(n^2) (best case), Ω(n^2) (worst case), Θ(n^2) (average case)

    Credit: @swapjs.ig on Instagram
    
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
    passes = 0
    while passes < len(working):
        for j in range(1, len(working)):
            if working[j-1] > working[j]:
                working[j-1], working[j] = working[j], working[j-1]
        passes += 1
        if len(working) >= 2 and random.random() < 0.4:
            i, j = random.sample(range(len(working)), 2)
            working[i], working[j] = working[j], working[i]
    result = sorted(working)
    if inPlace:
        data[:] = result
        return data
    return result