# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# 461. Hamming Distance
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
# Note:
# 0 ≤ x, y < 231. 
#
# Example:
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.


# brute-force solution! :(
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
    """
        xbits_str = str(bin(x)).lstrip('0b')
        ybits_str = str(bin(y)).lstrip('0b')

        xbits_len = len(xbits_str)
        ybits_len = len(ybits_str)
        # we need to fill in the leading zeros if one of them has shorter binary
        # representation.
        if xbits_len > ybits_len:
            ybits_str = "0" * (xbits_len - ybits_len) + ybits_str
        elif xbits_len < ybits_len:
            xbits_str = "0" * (ybits_len - xbits_len) + xbits_str

        # ^ is called bitwise exclusive or (XOR); 1 ^ 0 -> 1, 0 ^ 1 -> 1
        differences = [int(xy[0]) ^ int(xy[1]) for xy in zip(xbits_str, ybits_str)]
        hdistance = sum(differences)
        return hdistance
