# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys

if sys.version_info[0] < 3:
    range = xrange

def swap(ulist, index1, index2):
    """
    Swap two elements in a list and return the modified list.
    
    Parameters
    -----------
    ulist : list
    index1: int
    index2 : int

    Returns
    -------
    ulist : list
        The modified version of list after swap takes place.

    """
    
    ulist[index1], ulist[index2] = ulist[index2], ulist[index1]
    return ulist

def insertion_sort(ulist):
    """
    Return a sorted list at an increasing order.
    
    Assuming the first element in the list is sorted, and let such
    element in the list as the last_sorted. Do a pair-wise swap
    between the current element and its ancestors when the current
    element is smaller than its ancestor. Repeat the swap until
    the current element is larger than or equal to an ancestor
    element.

    Parameters
    ----------
    ulist : list
        An unsorted homogenous list.

    Returns
    -------
    slist : list
        A sorted list in an increasing order.

    """
    
    # assuming first element is sorted and always compare
    # with the previous element from current index
    for index in range(1, len(ulist)):
        if ulist[index] < ulist[index-1]:
            # compare with every ancestor from current index
            # if ancestor (given by prev_index) is bigger
            # than current index (given by prev_index+1), swap
            for prev_index in reversed(range(0, index)):
                if ulist[prev_index+1] < ulist[prev_index]:
                    ulist = swap(ulist, prev_index, prev_index+1)
                else:
                    break
    return ulist

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
