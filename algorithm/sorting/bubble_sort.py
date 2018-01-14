# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Bubble sort
#   For each element in an array of numbers, sort with the next number
#   until each element has been sorted.

import sys

if sys.version_info[0] < 3:
    range = xrange

def bubble_sort(arr):
    """
    >>> bubble_sort([])
    []
    >>> bubble_sort([1])
    [1]
    >>> bubble_sort([2,1])
    [1, 2]
    >>> bubble_sort([4,3,5,6])
    [3, 4, 5, 6]
    """

    length = len(arr)
    for i in range(length):
        for j in range(1, length - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr
