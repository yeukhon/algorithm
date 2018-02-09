# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# 686. Repeated String Match
# Given two strings A and B, find the minimum number of times A has to
# be repeated such that B is a substring of it. If no such solution,
# return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times (“abcdabcdabcd”),
# B is a substring of it; and B is not a substring of A repeated
# two times ("abcdabcd").
#
# Note:
# The length of A and B will be between 1 and 10000. 

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        count = 0
        new_a = ""
        while len(new_a) <= len(B):
            new_a += A
            count += 1
            if B in new_a:
                return count
        new_a += A
        if B in new_a:
            return count + 1
        return -1
