# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys

# Insertion sort
#   best case:      omega(n)    - only one comparison needed
#   worst case:     theta(n^2)
#   Big O:          O(n^2)

if sys.version_info[0] < 3:
    range = xrange

def insertion_sort(arr):
    """
    Return a sorted list in ascending order.

    Insertion sort works by assuming the first element in the
    array is "already sorted". We start with index i=1,
    and for each i, we compare backward (j=i-1, j=i-2 ..., j >= 0),
    and sawp array[j] and array[i] if array[i] > array[j].

    After the swap, we maintain this invariant:
        - on each pass, all elements before i are sorted.

    >>> insertion_sort([])
    []
    >>> insertion_sort([1])
    [1]
    >>> insertion_sort([2, 1])
    [1, 2]
    >>> insertion_sort([3, 5, 1, 6])
    [1, 3, 5, 6]

    """

    for i in range(1, len(arr)):
        # we use "reversed", which returns an iterator, to walk
        # backward of array.
        for j in reversed(range(i)):

            # if backward number is smaller, we swap
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def binary_insertion_sort(ulist):
    """
    Return a sorted list at an increasing order using binary search
    comparison instead of iterative comparison.

    Instead of iterative comparison, do a binary search on A[0:i-1].
    If A[i] < A[i/2], then it must be on the left (which are sorted).
    If A[i] > A[i/2], then it must be on the right (which are sorted).
    If A[i] == A[i/2], insert A[i] next to it.

    This still requires us to do Theta(n) swapping (in C or C++ you
    need to move individual pointer/element to make room for the 
    insertion.) In Python you combine lists and is quite expensive too.

    Parameters
    ----------
    ulist: list

    Returns
    -------
    slist: list

    """
    pass
