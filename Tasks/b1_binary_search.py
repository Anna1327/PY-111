from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if len(arr) == 0:
        return
    start = 0
    stop = (len(arr))
    while True:
        if start == stop:
            return None
        middle = ((stop - start) // 2) + start
        if elem == arr[middle]:
            return middle

        elif elem > arr[middle]:
            start = middle + 1

        elif elem < arr[middle]:
            stop = middle
