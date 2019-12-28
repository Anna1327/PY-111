"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    if len(arr) == 0:
        return

    min_ = arr[0]
    ind = 0
    for index, value in enumerate(arr):
        if value < min_:
            min_ = value
            ind = index
    return ind


def line_search(n, x):
    for index, value in enumerate(x):
        if value == n:
            return index
