# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# 349. Intersection of Two Arrays
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
#  - Each element in the result must be unique.
#  - The result can be in any order.
#
# Performance: O(n*m) where n = len(shorter_list), m = len(longer_list)

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if len(nums1) <= len(nums2):
            shorter_list = nums1
            longer_list = nums2
        else:
            shorter_list = nums2
            longer_list = nums1

        return [x for x in shorter_list if x in longer_list]
