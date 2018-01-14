# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import math

# Sum of array
#   Given an array of numbers, find the sum of the array.

def rsum(arr):
    """Returns the sum of an array of numbers.

    >>> rsum([])
    0

    >>> rsum([1,2])
    3

    >>> rsum([0.5, 0.3, 0.5])
    1.3

    """
    array_length = len(arr)

    if array_length == 0:
        return 0
    elif array_length == 1:
        return arr[0]
    elif array_length == 2:
        return arr[0] + arr[1]
    else:
        # Sum of the two sub-arrays.
        cut_at = int(math.floor(array_length/2))
        return (
            rsum(arr[:cut_at]) +
            rsum(arr[cut_at:])
        )
