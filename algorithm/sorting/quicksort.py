# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Quicksort
#   Given an array of numbers, sort the array in ascending order
#   using in-place recursion.
#   qsort(array) should be used.

def _quicksort(arr, low, high):
    """
    Quicksort works by selecting a random index from the array
    and called it "pivot". With the pivot, quicksort maintains the
    following invariants:

    1. elements left of the pivot, arr[left] <= pivot
    2. elements right of the pivot, arr[right] >= pivot

    """

#    print(arr, low, high)

    if len(arr) == 0:
        return arr

    if low < high:
        pivot_index = int(len(arr)/2)
        pivot = arr[pivot_index]

        i = low
        j = high

        #import pdb; pdb.set_trace()
        # swap pivot with the last element in the array
        arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]

        while i <= j:
            while arr[i] <= pivot and i <= j:
                i += 1
            while arr[j] >= pivot and j >= i:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[i], arr[pivot_index] = arr[pivot_index], arr[i]

        """
        # advance i (from left) until arr[i] >= pivot
        # or stop when i > high (end of the array)
        #while i < high and arr[i] <= pivot:
        while arr[i] < pivot:
            i += 1

        # advance j (from right) until arr[j] >= pivot
        # or stop when j < i
        while arr[j] > pivot:
#        while j < low and arr[j] >= pivot:
            j -= 1

        # we swap here because arr[i] and arr[j]
        # are still in the wrong side of the pivot
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            # when i and j cross, everything left to arr[i]
            # are less than or equal to pivot, so we can
            # stick pivot there
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]

            # then we recursively sort left of arr[i]
            # and arr[i+1]
            _quicksort(arr, low, i)
            _quicksort(arr, i+1, high)
    return arr
    """
        _quicksort(arr, low, i-1)
        _quicksort(arr, i+1, high)

def qsort(arr):
    """Return an array of numbers in ascending order.

    >>> qsort([])
    []

    >>> qsort([0])
    [0]

    >>> qsort([1, 2])
    [1, 2]

#    >>> qsort([3, 2, 1.1])
#    [1.1, 2, 3]

#    >>> qsort([2, 2, 2, 2])
#    [2, 2, 2, 2]

    >>> qsort([1, 6, 5])
    [1, 5, 6]

#    >>> qsort([1, 5, 6])
#    [1, 5, 6]

#    >>> qsort([5, 7, 11, 1, 2, 4, 8, 181])
#    [1, 2, 4, 5, 7, 8, 11, 181]

    """
    return _quicksort(arr, 0, len(arr)-1)

#if __name__ == "__main__":
#    print(
#        qsort([1, 5, 6])
#)
