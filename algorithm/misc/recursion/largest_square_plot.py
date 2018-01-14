# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Largest square plot problem
#
#   Given a M x N land, where m and n are both integers,
#   m >= 1 and n >=1, find the largest square-sized plot
#   the land can be divided into.
#
#   For example, given a 1680 x 640 land, the largest
#   square-sized plot is 80 x 80.

def largest_square_plot(width, height):
    """Given a ``width`` x ``height`` farm land,
    return the largest square-sized plot the farm
    land can be broken up into.

    >>> largest_square_plot(1680, 640)
    (80, 80)

    >>> largest_square_plot(25, 50)
    (25, 25)
    """

    # base case: stop dividing when we find the
    # largest square.
    if width == height:
        return width, height
    else:
        # otherwise, we know that we can break the land
        # into several pieces, some are already
        # square-sized, but there must be left over,
        # which is the difference of the wdith and height,
        # and can further divided.
        remain = abs(width - height)
        return largest_square_plot(remain,
            min([width, height]))
