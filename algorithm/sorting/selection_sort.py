# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Selection Sort
#   For each index i in an array of number, replace arr[i]
#   with arr[n] if arr[n] < arr[i], where {n > i, and n <= len(array)}
#
#   O(n^2) - since sum of (n-1, n-2, n-3, ..., 1)

import sys

if sys.version_info[0] < 3:
    range = xrange

def selection_sort(arr, start=None, end=None):
    """Return a sorted array in-place in ascending order
    by replacing each element in the array with the smallest
    number after its position.

    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    >>> selection_sort([2,1])
    [1, 2]
    >>> selection_sort([1,2,3])
    [1, 2, 3]

    """
    # compare last element with itself is a waste, so we can
    # i up to length of array - 1
    for i in range(0, len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def selection_sort_2(arr, start=None, end=None):
    """An enhanced selection sort with the ability to
    specify the range to sort.

    >>> selection_sort([])
    []
    >>> selection_sort([1])
    [1]
    >>> selection_sort([2,1])
    [1, 2]
    >>> selection_sort([1,2,3])
    [1, 2, 3]

    """

    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1

    for i in range(start, end):
        for j in range(i, end+1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
