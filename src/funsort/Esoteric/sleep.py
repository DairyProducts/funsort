from typing import Union

def sleep_sort(data:list[Union[int, float]], inPlace=False) -> list[Union[int, float]]:
    """
    Creates a new thread for each element in the list.

    Sleeps for a duration proportional to the value of the element,
    then appends the element to the output list. Only works for non-negative
    int and float values.

    Time complexity: O(n + max(data)) (best case), Ω(n) (worst case), Θ(n + max(data)) (average case)

    Args:
        data: A list to be sorted. Must contain only non-negative int or float values.
        inPlace: If True, sorts the list in place in addition to returning the sorted
            list. Otherwise, returns a new sorted list.

    Returns:
        The sorted list.
    """
    import threading
    import time

    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in the list must be int or float")
    if any(x < 0 for x in data):
        raise ValueError("All elements in the list must be non-negative")

    working = data if inPlace else data.copy()
    output = []
    threads = []

    def sleep_and_append(x):
        time.sleep(x)
        output.append(x)

    for x in working:
        thread = threading.Thread(target=sleep_and_append, args=(x,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if inPlace:
        data[:] = output
        return data
    return output
