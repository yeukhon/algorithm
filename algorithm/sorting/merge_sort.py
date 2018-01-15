# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
from algorithm.sorting.selection_sort import (
                            selection_sort,
                            selection_sort_2
)

# Merge sort
#   Merge sort works by dividing the input array into two sub-arrays
#   L1 and L2, and recursively divide until each sub-array reaches
#   size 0 or size 1.
#   At each level, selection sort is called on L1 and L2, yields
#   SL1 and SL2, concatenate SL1 and SL2, then return
#   the resulting sorted array.
#
#   Performance:
#    - 1 + upper(log n) levels
#    - each level takes O(n) due to selection sort
#    - requires extra N space (here we use 3*N)
#    Time complexity = theta (n log n) (best case, and worst case)
#
#   In-place version is more complex, but uses O(1) space.

if sys.version_info[0] < 3:
    range = xrange

def merge_sort(arr):
    """
    Return a copy of a sorted array in ascending order.

    >>> merge_sort([])
    []
    >>> merge_sort([1])
    [1]
    >>> merge_sort([1,2])
    [1, 2]
    >>> merge_sort([3, 4, 1])
    [1, 3, 4]
    >>> merge_sort([4, 4, 5, 1])
    [1, 4, 4, 5]
    """

    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        mid = int(len(arr)/2)

        u_list_1 = arr[:mid]
        u_list_2 = arr[mid:]

        s_list = (
            merge_sort(u_list_1) +
            merge_sort(u_list_2)
        )
        return selection_sort(s_list)

def ip_merge_sort(arr):
    """
    In-place version of merge sort on an array.

    >>> ip_merge_sort([])
    []
    >>> ip_merge_sort([1])
    [1]
    >>> ip_merge_sort([1,2])
    [1, 2]
    >>> ip_merge_sort([3, 4, 1])
    [1, 3, 4]
    >>> ip_merge_sort([4, 4, 5, 1])
    [1, 4, 4, 5]
    """

    def _merge(arr, start, end):
        if end-start == 0:
            return arr
        elif start == 0:
            mid = int(end/2)
        else:
            mid = int((end-start) / 2) + start

        _merge(arr, start, mid)
        _merge(arr, mid+1, end)

        return selection_sort_2(arr, start, end)

    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        return _merge(arr, 0, len(arr)-1)
